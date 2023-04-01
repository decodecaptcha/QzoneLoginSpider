# -*- coding: utf-8 -*-
# @Author : 艾登Aiden
# @Email : aiden2048@qq.com

import requests


class Request:
    def __new__(cls, *args, **kwargs):
        cls.meta = kwargs["meta"]
        del kwargs["meta"]
        cls.res = requests.request(*args, **kwargs)
        cls.res.meta = cls.meta
        return cls.res


class Response:
    def __init__(self):
        self.meta = {}
