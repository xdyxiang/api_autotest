# coding=utf8
import requests

def send_get(url,param,header):
    res = requests.get(url, params=param, headers=header)
    res_json = res.json()
    print("*" * 20)
    print("url地址：{0}".format(res.url))
    print("响应内容：{0}".format(res_json))
    print("*" * 100)
    return res_json


def send_post(url,body,header):
    res = requests.post(url, json=body, headers=header)
    res_json = res.json()
    print("*" * 20)
    print("url地址：{0}".format(res.url))
    print("请求内容：{0}".format(body))
    print("响应内容：{0}".format(res_json))
    print("*" * 100)
    return res_json

def send_delete(url,param,header):
    res = requests.delete(url, params=param, headers=header)
    res_json = res.json()
    print("*" * 20)
    print("url地址：{0}".format(res.url))
    print("响应内容：{0}".format(res_json))
    print("*" * 100)
    return res_json

def send_put(url,body,header):
    res = requests.put(url, json=body, headers=header)
    res_json = res.json()
    print("*" * 20)
    print("url地址：{0}".format(res.url))
    print("响应内容：{0}".format(res_json))
    print("*" * 100)
    return res_json
