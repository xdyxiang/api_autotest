# coding=utf8
import pytest
from verify_response.verify_base import verify_code_msg
from api_request.wallet_api.wallet_api import *
from common.config import settings

#  钱包ID:wid
wid_dev = ""
wid_pro = ""

if settings["env"] == "pro":
    wid = wid_pro
else:
    wid = wid_dev

expdata = {
    "code": 0,
    "message": "OK"
}


@pytest.mark.parametrize("coin", ["btc","bsv", "bch","ltc", "doge"])
def test_get_wallets_utxos(coin):
    """获取钱包UTXO"""
    data = {
        "coin": coin,
        "wid": wid
    }
    res = get_wallets_utxos(data)
    verify_code_msg(res, expdata)

@pytest.mark.parametrize("coin", ["btc", "bch", "ltc", "doge"])
def test_get_wallets_balance(coin):
    """获取钱包余额"""
    data = {
        "coin": coin,
        "wid": wid
    }
    res = get_wallets_balance(data)
    verify_code_msg(res, expdata)

@pytest.mark.parametrize("coin,io", [("btc",1), ("bch",-1), ("ltc",None), ("doge",1)])
def test_get_wallets_transactions(coin,io):
    """查询交易列表(分页)"""
    data = {
        "coin": coin,
        "wid": wid,
        "limit": 10,
        "page": 1,
        "io": io
    }
    res = get_wallets_transactions(data)
    verify_code_msg(res, expdata)

@pytest.mark.parametrize("coin", ["btc","bsv", "ltc", "doge"])
def test_send_wallets_transactions(coin):
    """发送交易"""
    data = {
        "coin": coin,
        "wid": wid,
        "tx_raw": "tx_raw"
    }
    expdata = {
        "code": 203,
        "message": "TX decode failed"
    }
    res = send_wallets_transactions(data)
    verify_code_msg(res, expdata)

@pytest.mark.parametrize("coin", ["btc", "bch", "ltc", "doge"])
def test_get_wallets_address(coin):
    """获取地址"""
    data = {
        "coin": coin,
        "wid": wid
    }
    res = get_wallets_address(data)
    verify_code_msg(res, expdata)
