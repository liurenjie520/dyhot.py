# coding=utf-8
"""
从土味情话中获取每日一句。
 """
from datetime import datetime

import requests
import json


__all__ = ['get_lovelive_info']


def get_lovelive_info():

    print('获取...')
    try:
        resp = requests.get('https://tenapi.cn/douyinresou/')
        if resp.status_code == 200:
            content_dict = resp.json()


            data = content_dict.get("list")
            result1 = []
            str24=""
            for i in data:
                result1.append(i.get("name"))




            for i in result1:
                kp = str(result1.index(i) + 1) + '.' + i + "\n\n"

                str24=str24+kp

            return str24
        print('获取失败。')
    except requests.exceptions.RequestException as exception:
        print(exception)
        # return None
    return None


get_one_words = get_lovelive_info

if __name__ == '__main__':
    is_tomorrow = get_lovelive_info()
    url = 'https://service-etcne5bg-1254304775.gz.apigw.tencentcs.com/release/Wecom_push'
    HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
    dt = datetime.now()
    time = dt.strftime('%Y-%m-%d')
    # 'application/x-www-form-urlencoded'
    # 'application/json;charset=utf-8'
    FormData = {
        'sendkey': 'akb48',
        'msg_type': 'text',
        'msg': f'抖音热榜-{time}'+'\n'+is_tomorrow

    }

    res = requests.post(url=url, json=FormData)
    # content = requests.post(url=url, data=FormData).text

    print(res.text)

    print(is_tomorrow)
