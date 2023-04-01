# -*- coding: utf-8 -*-
import json
import requests
from spiders.spider import Request, Response


def login(response, *args, **kwargs):
    _cookies = response.cookies.get_dict()
    response.meta["settings"]["COOKIES"].update(_cookies)
    cookies = response.meta["settings"]["COOKIES"]

    aid = response.meta["aid"]
    qq = response.meta["qq"]
    sid = response.meta["sid"]

    login_sig = cookies.get("pt_login_sig")
    ptdrvs =  cookies.get("ptdrvs") # 来自check 返回的ck中 ptdrvs

    assert response.text
    json_data = json.loads(response.text)
    randstr = json_data.get("randstr")
    ticket = json_data.get("ticket")

    url = f"https://ssl.ptlogin2.qq.com/login?u={qq}&verifycode={randstr}&pt_vcode_v1=1&pt_verifysession_v1={ticket}&p=KejBdf3UehrGtRUPLwmd7DCR1SWvQmcwkEHmKpjJDWeWBuzkCVOT3s24H0yJejfXI1Fvhr1yn-RVQMwLAht-OcFpuPa7e6W6Vu-LUkZ2pEF4Fzc7-MK-2Y*jLVZDg2XcZdW3MFStxWkK4l4ByDeN3ynJURqYb9ShHe09PS7pr8BQaaQLEx8OQaNW0VWNsC5nWcPiWHhe51uzJVrQWOqQSfEN3yOJK3*BMSuaRJXozhMPjwQKWD2zTm4Uq5g48MON4Sq3BIOSxImpIW7eJVaPiPjLqJKswwffiGUeOFUuZGNE*z2wEWu*R79PJELC8W541xqzy3P6k2qZQ0upoSJG8Q__&pt_randsalt=2&u1=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&ptredirect=0&h=1&t=1&g=1&from_ui=1&ptlang=2052&action=4-9-1679898821804&js_ver=23010412&js_type=1&login_sig={login_sig}&pt_uistyle=40&aid={aid}&daid=5&ptdrvs={ptdrvs}&sid={sid}&&o1vId=95f35f6d6fa7bf11b07025c6259e9919&pt_js_version=v1.41.0"

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
        cookies=cookies,
        data=payload,
        meta=response.meta,
        *args,
        **kwargs
    )
