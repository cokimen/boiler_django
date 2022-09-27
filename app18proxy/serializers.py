from rest_framework.status import is_client_error
from rest_framework.exceptions import APIException, ValidationError
from django.conf import settings
import requests
from urllib.parse import urljoin
from json.decoder import JSONDecodeError
import traceback
from rest_framework.serializers import Serializer
from requesthelper import RequestHelper
import uuid


class ProxySerializer(Serializer):

    def __init__(self, *args, **kwargs):
        super(ProxySerializer, self).__init__(*args, **kwargs)
        self.response = None  # type: Optional[dict]

    def get_proxy_host(self):
        raise NotImplementedError("method get_proxy_host() must be overridden")

    def get_proxy_route(self):
        raise NotImplementedError(
            "method get_proxy_route() must be overridden")

    def get_url_proxy(self) -> str:
        raise NotImplementedError("method get_url_proxy() must be overridden")

    def get_request_headers(self) -> dict:
        raise NotImplementedError(
            "method get_request_headers() must be overridden")

    def get_payload(self, attrs):
        """
        :param attrs:
        :return:
        you can override this.
        """
        return attrs

    def _serialize_payload(self, payload):
        for key, value in payload.copy().items():
            if isinstance(value, uuid.UUID):
                payload[key] = value.hex

    def proxy(self, attrs):
        payload = self.get_payload(attrs)
        self._serialize_payload(payload)
        request = self.context.get('request')
        helper = RequestHelper(self.get_proxy_host())
        kwargs = {
            "method": request.method.lower(),
            "url": self.get_url_proxy(),
            "json": payload
        }
        if request.FILES:
            kwargs.pop('json')
            for key, value in request.FILES.items():
                payload.pop(key)

            kwargs.update({
                'data': payload,
                'files': request.FILES
            })
        response = helper.request(**kwargs)
        self.response = helper.get_json()
        return response

    def validate(self, attrs):
        attrs = super(ProxySerializer, self).validate(attrs)
        self.proxy(attrs=attrs)
        return attrs

    def create(self, validated_data):
        return self.response


class StakingProxySerializer(ProxySerializer):

    def proxy(self, attrs):
        payload = self.get_payload(attrs)
        uid = payload['user_id']
        payload['user_id'] = str(uid)
        self._serialize_payload(payload)
        request = self.context.get('request')
        helper = RequestHelper(self.get_proxy_host())
        kwargs = {
            "method": 'post',
            "url": self.get_url_proxy(),
            "json": payload
        }
        if request.FILES:
            kwargs.pop('json')
            for key, value in request.FILES.items():
                payload.pop(key)

            kwargs.update({
                'data': payload,
                'files': request.FILES
            })
        print(payload)
        response = helper.request(**kwargs)
        self.response = helper.get_json()
        return response

    def get_proxy_host(self):
        return settings.STAKING_SERVICE_URL

    def get_url_proxy(self) -> str:
        return urljoin(self.get_proxy_host(), self.get_proxy_route())

    def get_request_headers(self) -> dict:
        return {
            'Authorization': settings.STAKING_AUTH_HEADER
        }
