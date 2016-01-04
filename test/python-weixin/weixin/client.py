# -*-coding: utf-8 -*-
# !/usr/bin/env python
from __future__ import unicode_literals

"""
File:   client.py
Author: goodspeed
Email:  cacique1103@gmail.com
Github: https://github.com/zongxiao
Date:   2015-02-06
Description: Weixin OAuth2
"""

from . import oauth2
from .bind import bind_method
from .helper import genarate_signature


SUPPORTED_FORMATS = ['', 'json']


class WeixinAPI(oauth2.OAuth2API):

    host = "open.weixin.qq.com"
    base_path = ""
    access_token_field = "access_token"
    authorize_url = "https://open.weixin.qq.com/connect/qrconnect"
    access_token_url = "https://api.weixin.qq.com/sns/oauth2/access_token"
    refresh_token_url = "https://api.weixin.qq.com/sns/oauth2/refresh_token"
    protocol = "https"
    api_name = "Weixin"
    x_ratelimit_remaining = None
    x_ratelimit = None

    def __init__(self, *args, **kwargs):
        format = kwargs.get('format', '')
        if format in SUPPORTED_FORMATS:
            self.format = format
        else:
            raise Exception("Unsupported format")
        super(WeixinAPI, self).__init__(*args, **kwargs)

    validate_token = bind_method(path='/sns/auth',
                                 accepts_parameters=['openid'],
                                 response_type="entry")

    user = bind_method(path="/sns/userinfo",
                       accepts_parameters=["openid"],
                       response_type="entry")


class WeixinMpAPI(oauth2.OAuth2API):

    host = "open.weixin.qq.com"
    base_path = ""
    access_token_field = "access_token"
    authorize_url = "https://open.weixin.qq.com/connect/oauth2/authorize"
    access_token_url = "https://api.weixin.qq.com/sns/oauth2/access_token"
    refresh_token_url = "https://api.weixin.qq.com/sns/oauth2/refresh_token"
    client_credential_token_url = "https://api.weixin.qq.com/cgi-bin/token"
    protocol = "https"
    api_name = "WeixinMp"
    x_ratelimit_remaining = None
    x_ratelimit = None

    def __init__(self, *args, **kwargs):
        self.mp_token = kwargs.get('mp_token', None)
        self.timestamp = kwargs.get('timestamp', None)
        self.nonce = kwargs.get('nonce', None)
        self.signature = kwargs.get('signature', None)
        self.echostr = kwargs.get('echostr', None)
        self.xml_body = kwargs.get('xml_body', None)
        self.grant_type = kwargs.get('grant_type', None)
        format = kwargs.get('format', '')

        if format in SUPPORTED_FORMATS:
            self.format = format
        else:
            raise Exception("Unsupported format")
        super(WeixinMpAPI, self).__init__(*args, **kwargs)

    def validate_signature(self):
        params = {
            'timestamp': self.timestamp,
            'token': self.mp_token,
            'nonce': self.nonce
        }
        signature = genarate_signature(params)
        return signature == self.signature

    user = bind_method(path="/sns/userinfo",
                       accepts_parameters=["openid"],
                       response_type="entry")

    jsapi_ticket = bind_method(path='/cgi-bin/ticket/getticket',
                               accepts_parameters=['type'],
                               response_type="entry")

