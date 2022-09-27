from urllib import request
import requests


def wrapper_request(method, body_payload={}, form=None) -> object:
    if method == 'post':
        requests.post
    if method == 'get':
        requests.get
    if method == 'patch':
        requests.patch
    if method == 'put':
        requests.put
    if method == 'delete':
        requests.delete
