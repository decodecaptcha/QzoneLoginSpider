# -*- coding: utf-8 -*-
import json
import random
from loguru import logger
from spiders.spider import Request, Response


def txcaptcha(response, *args, **kwargs):
    _cookies = response.cookies.get_dict() # ptdrvs
    response.meta["settings"]["COOKIES"].update(_cookies)
    cookies = response.meta["settings"]["COOKIES"]

    aid = response.meta["aid"]
    result = response.text.split(",")
    sid = result[-1].strip('")').strip("')")
    response.meta["sid"] = sid
    entry_url = 'https%3A%2F%2Fxui.ptlogin2.qq.com%2Fcgi-bin%2Fxlogin'
    callback = f"_aq_{random.randint(100, 999)}{random.randint(100, 999)}"
    start_url = f'https://t.captcha.qq.com/cap_union_prehandle?aid={aid}&protocol=https&accver=1&showtype=embed&ua=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk1LjAuNDYzOC42OSBTYWZhcmkvNTM3LjM2&noheader=1&fb=1&aged=0&enableAged=0&enableDarkMode=0&sid={sid}&grayscale=1&clientype=2&cap_cd=&uid=&lang=zh-cn&entry_url={entry_url}&elder_captcha=0&js=%2Ftcaptcha-frame.30646403.js&login_appid=&wb=2&subsid=5&callback={callback}&sess='

    # 本地 http 服务
    url = "http://localhost:8000/txcaptcha?user=temp"

    settings = response.meta["settings"]
    settings["START_URL"] = start_url

    logger.info(f'PROXIES===>{settings["PROXIES"]}')
    logger.debug(f'prehandle url===>{settings["START_URL"]}')
    payload = json.dumps(settings)

    headers = {
        'Content-Type': 'application/json'
    }
    return Request(
        url=url,
        method="POST",
        headers=headers,
        cookies=cookies,
        data=payload,
        meta=response.meta,
        *args,
        **kwargs
    )