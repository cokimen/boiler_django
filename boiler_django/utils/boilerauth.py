from django.conf import settings
from rest_framework.permissions import AllowAny
from app7auth.models import BoilerAuth


class BoilerTokenAuth(AllowAny):

    def has_permission(self, request, view):
        try:
            prefix, key = request.META.get('HTTP_AUTHORIZATION').split(' ')
        except Exception:
            return False
        else:
            try:
                auth = BoilerAuth.objects.get(keytoken=key)
                return True
            except BoilerAuth.DoesNotExist as e:
                # you musy know to use raise and return in except
                return False
