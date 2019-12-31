# coding=utf8

from urllib import parse
import json
from common.tool import get_time_stamp, hash_encrypt,get_baseurl
from common.send_func import send_get,send_post,send_put,send_delete
base_url = get_baseurl()

def get_account(data):
    """获取账户信息"""
    api_key = data["api_key"]
    url = base_url + "openapi/v1/account"
    header = {
        "X-API-KEY": api_key
    }
    param = None
    res = send_get(url, param, header)
    return res


def get_account_sub(data):
    """获取子账户列表"""
    api_key = data["api_key"]
    secret_key = data["secret_key"]
    page = data["page"]
    limit = data["limit"]
    tonce = get_time_stamp()
    if data.get("tonce"):
        tonce = data.get("tonce")
    url = base_url + "openapi/v1/account/sub"
    param = {
        "tonce": tonce,
        "page": page,
        "limit": limit
    }
    # 加密参数
    query_string = parse.urlencode(param)
    sign = hash_encrypt(secret_key, query_string)
    header = {
        "X-API-KEY": api_key,
        "X-SIGNATURE": sign,
    }
    res = send_get(url, param, header)
    return res


def create_account_sub(data):
    """创建子账户"""
    api_key = data["api_key"]
    secret_key = data["secret_key"]
    account = data["account"]
    tonce = get_time_stamp()
    if data.get("tonce"):
        tonce = data.get("tonce")
    url = base_url + "openapi/v1/account/sub"
    body = {
        "tonce": tonce,
        "account": account
    }
    sign = hash_encrypt(secret_key, json.dumps(body))
    header = {
        "X-API-KEY": api_key,
        "X-SIGNATURE": sign,
        "Content-Type": "application/json"
    }
    res = send_post(url, body, header)
    return res


def get_observer(data):
    """获取观察者列表"""
    api_key = data["api_key"]
    page = data["page"]
    limit = data["limit"]
    param = {
        "page": page,
        "limit": limit
    }
    url = base_url + "openapi/v1/account/observer"
    header = {
        "X-API-KEY": api_key
    }
    res = send_get(url,param,header)
    return res


def create_observer(data):
    """创建观察者"""
    api_key = data["api_key"]
    secret_key = data["secret_key"]
    obsname = data["obsname"]
    tonce = get_time_stamp()
    if data.get("tonce"):
        tonce = data.get("tonce")
    url = base_url + "openapi/v1/account/observer"
    body = {
        "tonce": tonce,
        "name": obsname
    }
    sign = hash_encrypt(secret_key, json.dumps(body))
    header = {
        "X-API-KEY": api_key,
        "X-SIGNATURE": sign,
        "Content-Type": "application/json"
    }
    res = send_post(url, body, header)
    return res


def create_sub_aggregate(data):
    """创建子账户-聚合
    该接口创建一个子账户和观察者，并设置自动提现地址"""
    api_key = data["api_key"]
    secret_key = data["secret_key"]
    account = data["account"]
    observer_name = data["obsname"]
    withdraw_address = data["withdraw_address"]
    tonce = get_time_stamp()
    if data.get("tonce"):
        tonce = data.get("tonce")
    url = base_url + "openapi/v1/account/sub/aggregate"
    body = {
        "tonce": tonce,
        "account": account,
        "observer_name": observer_name,
        "withdraw_address": withdraw_address
    }
    sign = hash_encrypt(secret_key, json.dumps(body))
    header = {
        "X-API-KEY": api_key,
        "X-SIGNATURE": sign,
        "Content-Type": "application/json"
    }
    res = send_post(url, body, header)
    return res


def get_account_group(data):
    """矿工分组列表"""
    api_key = data["api_key"]
    coin = data["coin"]
    url = base_url + "openapi/v1/account/group"
    param = {
        "coin": coin,
    }
    header = {
        "X-API-KEY": api_key,
    }
    res = send_get(url, param, header)
    return res


def create_account_group(data):
    """新建矿工分组"""
    api_key = data["api_key"]
    secret_key = data["secret_key"]
    coin = data["coin"]
    group_name = data["group_name"]
    tonce = get_time_stamp()
    if data.get("tonce"):
        tonce = data.get("tonce")
    url = base_url + "openapi/v1/account/group"
    body = {
        "tonce": tonce,
        "coin": coin,
        "group_name": group_name,
    }
    sign = hash_encrypt(secret_key, json.dumps(body))
    header = {
        "X-API-KEY": api_key,
        "X-SIGNATURE": sign,
        "Content-Type": "application/json"
    }
    res = send_post(url, body, header)
    return res


def put_account_group(data):
    """移动矿工分组"""
    api_key = data["api_key"]
    secret_key = data["secret_key"]
    worker_ids = data["worker_ids"]
    group_id = data["group_id"]
    tonce = get_time_stamp()
    if data.get("tonce"):
        tonce = data.get("tonce")
    url = base_url + "openapi/v1/account/group"
    body = {
        "tonce": tonce,
        "worker_ids": worker_ids,
        "group_id": group_id,
    }
    sign = hash_encrypt(secret_key, json.dumps(body))
    header = {
        "X-API-KEY": api_key,
        "X-SIGNATURE": sign,
        "Content-Type": "application/json"
    }
    res = send_put(url, body, header)
    return res


def delete_account_group(data):
    """删除矿工分组"""
    api_key = data["api_key"]
    secret_key = data["secret_key"]
    group_id = data["group_id"]
    tonce = get_time_stamp()
    if data.get("tonce"):
        tonce = data.get("tonce")
    url = base_url + "openapi/v1/account/group/{0}".format(group_id)
    param = {
        "tonce":tonce
    }
    # 加密参数
    query_string = parse.urlencode(param)
    sign = hash_encrypt(secret_key, query_string)
    header = {
        "X-API-KEY": api_key,
        "X-SIGNATURE": sign,
        "Content-Type": "application/json"
    }
    res = send_delete(url, param, header)
    return res
