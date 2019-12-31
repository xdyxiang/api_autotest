# coding=utf8

import json
from common.send_func import send_get,send_post
from common.tool import get_time_stamp, hash_encrypt,get_baseurl


base_url = get_baseurl()

def set_wallet_payment_address(data):
    """设置自动提现地址"""
    api_key = data["api_key"]
    secret_key = data["secret_key"]
    coin = data["coin"]
    address = data["address"]
    payment_password = data["payment_password"]
    url = base_url + "openapi/v1/wallet/payment/address"
    tonce = get_time_stamp()
    if data.get("tonce"):
        tonce = data.get("tonce")
    body = {
        "tonce": tonce,
        "coin": coin,
        "address": address,
        "payment_password": payment_password
    }
    sign = hash_encrypt(secret_key, json.dumps(body))
    header = {
        "X-API-KEY": api_key,
        "X-SIGNATURE": sign,
        "Content-Type": "application/json"
    }
    res = send_post(url, body, header)
    return res


def get_wallet_payment_history(data):
    """获取账户支付记录"""
    api_key = data["api_key"]
    coin = data["coin"]
    start_date = data["start_date"]
    end_date = data["end_date"]
    utc = data["utc"]
    page = data["page"]
    limit = data["limit"]
    param = {
        "coin": coin,
        "start_date": start_date,
        "end_date": end_date,
        "utc": utc,
        "page": page,
        "limit": limit
    }
    url = base_url + "openapi/v1/wallet/payment/history"
    header = {
        "X-API-KEY": api_key
    }
    res = send_get(url,param,header)
    return res


def get_profit(data):
    """获取账户收益信息"""
    api_key = data["api_key"]
    coin = data["coin"]
    param = {
        "coin": coin
    }
    url = base_url + "openapi/v1/profit"
    header = {
        "X-API-KEY": api_key
    }
    res = send_get(url,param,header)
    return res


def get_profit_history(data):
    """获取账户历史收益"""
    api_key = data["api_key"]
    coin = data["coin"]
    start_date = data["start_date"]
    end_date = data["end_date"]
    utc = data["utc"]
    page = data["page"]
    limit = data["limit"]
    param = {
        "coin": coin,
        "start_date": start_date,
        "end_date": end_date,
        "utc": utc,
        "page": page,
        "limit": limit,
    }
    url = base_url + "openapi/v1/profit/history"
    header = {
        "X-API-KEY": api_key
    }
    res = send_get(url,param,header)
    return res


# 指定某个账号才能结算钱包余额（自动提现）
def wallet_sweep(data):
    """结算钱包余额"""
    api_key = data["api_key"]
    secret_key = data["secret_key"]
    coin = data["coin"]
    tonce = get_time_stamp()
    if data.get("tonce"):
        tonce = data.get("tonce")

    url = base_url + "openapi/v1/wallet/sweep"
    body = {
        "tonce": tonce,
        "coin": coin,
    }
    sign = hash_encrypt(secret_key, json.dumps(body))
    header = {
        "X-API-KEY": api_key,
        "X-SIGNATURE": sign,
        "Content-Type": "application/json"
    }
    res = send_post(url, body, header)
    return res

# 指定某个账号才能提现（普通提现）
def wallet_withdraw(data):
    """提现"""
    api_key = data["api_key"]
    secret_key = data["secret_key"]
    coin = data["coin"]
    address = data["address"]
    amount = data["amount"]
    payment_password = data["payment_password"]
    tonce = get_time_stamp()
    if data.get("tonce"):
        tonce = data.get("tonce")

    url = base_url + "openapi/v1/wallet/withdraw"
    body = {
        "tonce": tonce,
        "coin": coin,
        "address": address,
        "amount": amount,
        "payment_password": payment_password,
    }
    sign = hash_encrypt(secret_key, json.dumps(body))
    header = {
        "X-API-KEY": api_key,
        "X-SIGNATURE": sign,
        "Content-Type": "application/json"
    }
    res = send_post(url, body, header)
    return res
