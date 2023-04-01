# -*- coding: utf-8 -*-
import json
import re
from spiders.spider import Request, Response

def check(response, *args, **kwargs):
    qq = response.meta["qq"]
    _cookies = response.cookies.get_dict()
    response.meta["settings"]["COOKIES"].update(_cookies)
    cookies = response.meta["settings"]["COOKIES"]
    
    login_sig = _cookies.get("pt_login_sig")
    url = f"https://ssl.ptlogin2.qq.com/check?regmaster=&pt_tea=2&pt_vcode=1&uin={qq}&appid=549000912&js_ver=23010412&js_type=1&login_sig={login_sig}&u1=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&r=0.7759239664923412&pt_uistyle=40&daid=5&pt_3rd_aid=0&o1vId=95f35f6d6fa7bf11b07025c6259e9919&pt_js_version=v1.41.0"
    
    payload={}
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '"Chromium";v="21", " Not;A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        "User-Agent": response.meta["settings"]["USER_AGENT"],
        'sec-ch-ua-platform': '"Windows"',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Dest': 'script',
        'Referer': 'https://xui.ptlogin2.qq.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    return Request(
        url=url,
        method="GET",
        headers=headers,
        data=payload,
        cookies=cookies,
        meta=response.meta,
        *args,
        **kwargs
    )
