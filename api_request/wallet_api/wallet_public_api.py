# coding=utf8

from common.tool import get_baseurl
from common.send_func import send_get,send_post
base_url = get_baseurl("wallet")
app_header = {
   "X-Platform":"iOS",
   "X-Build":"47",
   "X-Version":"1.1.1",
}

def create_wallets_wid(data):
    """通过key获取wid"""
    key = data["key"]  # BTC的拓展公钥
    url = base_url + "wallets/wid"
    header = {
    }
    body = {
        "key":key
    }
    res = send_post(url, body, header)
    return res


def pull_wallets_balance(data):
    """获取所有币的余额"""
    wid = data["wid"]
    coinlist = data["coinlist"]
    url = base_url + "wallets/balance"
    header = {
        "X-WID":wid
    }
    body = coinlist
    res = send_post(url, body, header)
    return res

def create_wallets_init(data):
    """注册钱包"""
    wid = data["wid"]
    btc_xpub = data["btc_xpub"]
    ltc_xpub = data["ltc_xpub"]
    bch_xpub = data["bch_xpub"]
    doge_xpub = data["doge_xpub"]
    url = base_url + "wallets/init"
    header = {
        "X-WID":wid
    }
    body = {
        "btc_xpub":btc_xpub,
        "ltc_xpub":ltc_xpub,
        "bch_xpub":bch_xpub,
        "doge_xpub":doge_xpub,
    }
    res = send_post(url,body, header)
    return res

def get_fee(data):
    """获取手续费"""
    coin = data["coin"]  # 小写
    url = base_url + "fee/{0}".format(coin)
    header = {
    }
    param = None
    res = send_get(url, param, header)
    return res

def get_exchange():
    """获取汇率支持的法币"""
    url = base_url + "exchange"
    header = {
    }
    param = None
    res = send_get(url, param, header)
    return res

def get_exchange_currency(data):
    """获取指定法币对应的数字货币汇率"""
    currency = data["currency"]
    url = base_url + "exchange/{0}".format(currency)
    header = {
    }
    param = {}
    res = send_get(url, param, header)
    return res


def get_version(data):
    """获取指定法币对应的数字货币汇率"""
    """  指定iOS:
        User-Agent: ViaWallet/1.0.0 (com.viabtc.ViaWallet; build:26; iOS 12.2.0) Alamofire/4.8.0
        指定Android:
        User-Agent: ViaWallet/1.0.0 (com.viabtc.ViaWallet; build:26; Android 12.2.0) Alamofire/4.8.0
        指定简体中文:
        Accept-Language:zh_Hans_CN;q=1.0
        指定繁体中文:
        Accept-Language:zh_Hant_HK;q=1.0
        指定英文:
        Accept-Language:en_US;q=1.0"""

    useragent = data["useragent"]
    language = data["language"]
    url = base_url + "version"
    header = {
        "User-Agent":useragent,
        "Accept-Language":language
    }
    header.update(app_header)
    param = None
    res = send_get(url, param, header)
    return res



def get_msg(data):
    """获取消息列表"""
    wid = data["wid"]
    limit = data["limit"] # 每页条数
    # time = data["time"] # 上一页最后一条的时间
    url = base_url + "wallets/msg/tx"
    header = {
        "X-WID": wid
    }
    param = {
        "limit":limit,
        "time":None
    }
    res = send_get(url, param, header)
    return res


def all_read_msg(data):
    """消息全部已读"""
    wid = data["wid"]
    url = base_url + "wallets/msg/tx"
    header = {
        "X-WID": wid
    }
    body = {}
    res = send_post(url, body, header)
    return res

def get_msg_detail(data):
    """获取消息详情"""
    wid = data["wid"]
    msgid = data["msgid"]
    url = base_url + "wallets/msg/tx/{0}".format(msgid)
    header = {
        "X-WID": wid
    }
    param = None
    res = send_get(url, param, header)
    return res


def get_msg_unread(data):
    """获取未读消息条数"""
    wid = data["wid"]
    url = base_url + "wallets/msg/unread"
    header = {
        "X-WID": wid
    }
    param = None
    res = send_get(url, param, header)
    return res

def get_stake():
    """获取Staking币种列表"""
    url = base_url + "stake"
    header = {}
    param = None
    res = send_get(url, param, header)
    return res
