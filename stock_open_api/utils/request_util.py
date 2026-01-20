# -*- coding: utf-8 -*-
"""
@File    : request_util.py
@Date    : 2023-07-18

a requests wrapper
"""

import requests

from stock_open_api.utils import ua_util

default_headers = {
    'User-Agent': ua_util.User_Agent
}

tt_headers = {
  "validmark":
    'aKVEnBbJF9Nip2Wjf4de/fSvA8W3X3iB4L6vT0Y5cxvZbEfEm17udZKUD2qy37dLRY3bzzHLDv+up/Yn3OTo5Q==',
}


deviceId = '874C427C-7C24-4980-A835-66FD40B67605'
version = '6.5.5'
baseData = {
  "product": 'EFund',
  "deviceid": deviceId,
  "MobileKey": deviceId,
  "plat": 'Iphone',
  "PhoneType": 'IOS15.1.0',
  "OSVersion": '15.5',
  "version":version,
  "ServerVersion": version,
  "Version": version,
  "appVersion": version,
}


def request(method, url, **kwargs):
    kwargs.setdefault('headers', default_headers)
    return requests.request(method, url, **kwargs)


def get(url, params=None, **kwargs):
    return request("get", url, params=params, **kwargs)


def post(url, data=None, json=None, **kwargs):
    return request("post", url, data=data, json=json, **kwargs)


def post_ttjj(url, data=None, json=None, **kwargs):
    kwargs.setdefault('headers', tt_headers)
    data.update(baseData)
    return request("post", url, data=data, json=json, **kwargs)
