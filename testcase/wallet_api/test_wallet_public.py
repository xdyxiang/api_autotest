# coding=utf8

from verify_response.verify_base import verify_code_msg
from api_request.wallet_api.wallet_public_api import *
from common.config import settings

#  钱包ID:xwid   拓展公钥(xkey)  -----用拓展公钥生成钱包ID
key_dev = ""  # 测试环境
wid_dev = ""
key_pro = ""  # 生产环境
wid_pro = ""

if settings["env"] == "pro":
    wid = wid_pro
    key = key_pro
else:
    wid = wid_dev
    key = key_dev

expdata = {
    "code": 0,
    "message": "OK"
}


def test_get_wallets_wid():
    """通过key获取wid"""
    data = {"key": key}
    res = create_wallets_wid(data)
    verify_code_msg(res, expdata)


def test_pull_wallets_balance():
    """获取所有币的余额"""
    data = {"wid": wid, "coinlist": ["BTC","bch","ltc","doge"]}
    print(data)
    res = pull_wallets_balance(data)
    verify_code_msg(res, expdata)


def test_create_wallets_init():
    """注册钱包"""
    data = {"wid": wid,
            "btc_xpub": "",
            "bch_xpub": "", "ltc_xpub": "", "doge_xpub": ""}
    res = create_wallets_init(data)
    verify_code_msg(res, expdata)


def test_get_fee():
    """获取手续费"""
    data = {"coin": "btc"}
    res = get_fee(data)
    verify_code_msg(res, expdata)


def test_get_exchange():
    """获取汇率支持的法币"""
    res = get_exchange()
    verify_code_msg(res, expdata)


def test_get_exchange_currency():
    """获取指定法币对应的数字货币汇率"""
    data = {"currency": "CNY"}
    res = get_exchange_currency(data)
    verify_code_msg(res, expdata)


def test_get_version():
    """获取APP版本信息"""
    data = {"useragent": "/1.0.0 (com.viabtc.ViaWallet; build:26; iOS 12.2.0) Alamofire/4.8.0",
            "language": "zh_Hans_CN;q=1.0"}
    res = get_version(data)
    verify_code_msg(res, expdata)


def test_get_msg():
    """获取消息列表"""
    data = {
        "wid":wid,
        "limit":10
    }
    res = get_msg(data)
    verify_code_msg(res, expdata)


def test_all_read_msg():
    """消息全部已读"""
    data = {
        "wid":wid,
    }
    res = all_read_msg(data)
    verify_code_msg(res, expdata)

def test_get_msg_detail():
    """获取消息详情"""
    data = {
        "wid": wid,
        "msgid": "xxxx"
    }
    expdata = {
        "code": 2,
        "message": "Invalid argument"
    }
    res = get_msg_detail(data)
    verify_code_msg(res, expdata)

def test_get_msg_unread():
    """获取未读消息条数"""
    data = {
        "wid": wid
    }
    res = get_msg_unread(data)
    verify_code_msg(res, expdata)

def test_get_stake():
    """获取Staking币种列表"""
    res = get_stake()
    verify_code_msg(res, expdata)
