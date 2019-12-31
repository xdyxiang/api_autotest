# coding=utf8
import pytest
from api_request.openapi.wallet_api import *
from verify_response.verify_base import verify_code_msg
from common.readfile import *

data_file = get_filepath(__file__)


@pytest.mark.parametrize("data", getdata(data_file, "test_set_wallet_payment_address"))
def test_set_wallet_payment_address(data):
    """设置自动提现地址"""
    res = set_wallet_payment_address(data["reqdata"])
    verify_code_msg(res, data["expdata"])

@pytest.mark.parametrize("data", getdata(data_file, "test_get_wallet_payment_history"))
def test_get_wallet_payment_history(data):
    """获取账户支付记录"""
    res = get_wallet_payment_history(data["reqdata"])
    verify_code_msg(res, data["expdata"])

@pytest.mark.parametrize("data", getdata(data_file, "test_get_profit"))
def test_get_profit(data):
    """获取账户收益信息"""
    res = get_profit(data["reqdata"])
    verify_code_msg(res, data["expdata"])

@pytest.mark.parametrize("data", getdata(data_file, "test_get_profit_history"))
def test_get_profit_history(data):
    """获取账户历史收益"""
    res = get_profit_history(data["reqdata"])
    verify_code_msg(res, data["expdata"])

@pytest.mark.parametrize("data", getdata(data_file, "test_wallet_sweep"))
def test_wallet_sweep(data):
    """结算钱包余额
    只有特定账号才能有权限请求"""
    res = wallet_sweep(data["reqdata"])
    verify_code_msg(res, data["expdata"])


@pytest.mark.parametrize("data", getdata(data_file, "test_wallet_withdraw"))
def test_wallet_withdraw(data):
    """提现（普通提现）
    只有特定账号才能有权限请求"""
    res = wallet_withdraw(data["reqdata"])
    # verify_code_msg(res, data["expdata"])
