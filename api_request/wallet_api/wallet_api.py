# coding=utf8
from common.tool import get_baseurl
from common.send_func import send_get,send_post
base_url = get_baseurl("wallet")

# app_header_ios = {
#    "X-Platform":"iOS",
#    "X-Build":"47",
#    "X-Version":"1.1.1",
# }
# app_header_android = {
#    "X-Platform":"iOS",
#    "X-Build":"39",
#    "X-Version":"1.1.0",
# }
app_header = {}

def get_wallets_utxos(data):
    """获取钱包UTXO"""
    coin = data["coin"]
    wid = data["wid"]
    url = base_url + "{0}/wallets/utxos".format(coin)
    header = {
        "X-WID": wid
    }
    header.update(app_header)
    param = None
    res = send_get(url, param, header)
    return res

def get_wallets_balance(data):
    """获取钱包余额(根据拓展公钥)"""
    coin = data["coin"]  # btc
    wid = data["wid"]
    url = base_url + "{0}/wallets/balance".format(coin)
    header = {
        "X-Wid": wid
    }
    header.update(app_header)
    param = None
    res = send_get(url, param, header)
    return res


def get_wallets_transactions(data):
    """查询交易列表(分页)"""
    coin = data["coin"]  # btc
    wid = data["wid"]
    limit = data["limit"]
    page = data["page"]
    io = data["io"]
    url = base_url + "{0}/wallets/transactions".format(coin)
    header = {
        "X-Wid": wid
    }
    header.update(app_header)
    param = {
    "limit": limit,
    "page": page,
    "io": io        # io为-1表示发送，1表示接收，空表示所有
    }
    res = send_get(url, param, header)
    return res


def send_wallets_transactions(data):
    """发送交易"""
    coin = data["coin"]  # btc
    tx_raw = data["tx_raw"]
    wid = data["wid"]
    url = base_url + "{0}/transactions".format(coin)
    body = {
    "tx_raw": tx_raw
    }
    header = {
        "X-Wid": wid
    }
    header.update(app_header)
    res = send_post(url, body, header)
    return res


def get_wallets_address(data):
    """获取地址
    找零地址/收款地址"""
    coin = data["coin"]  # btc
    wid = data["wid"]
    url = base_url + "{0}/wallets/address".format(coin)
    header = {
        "X-Wid": wid
    }
    header.update(app_header)
    param = None
    res = send_get(url, param, header)
    return res

