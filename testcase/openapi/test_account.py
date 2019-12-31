# coding=utf8
import pytest
from api_request.openapi.account_api import *
from verify_response.verify_base import verify_code_msg
from common.readfile import *
from common.config import settings

data_file = get_filepath(__file__)


@pytest.mark.parametrize("data", getdata(data_file, "test_get_account"))
def test_get_account(data):
    """获取账户信息"""
    res = get_account(data["reqdata"])
    verify_code_msg(res, data["expdata"])


@pytest.mark.parametrize("data", getdata(data_file, "test_get_account_sub"))
def test_get_account_sub(data):
    """获取子账户列表"""
    res = get_account_sub(data["reqdata"])
    verify_code_msg(res, data["expdata"])


@pytest.mark.parametrize("data", getdata(data_file, "test_create_account_sub"))
def test_create_account_sub(data):
    """创建子账户"""
    # print(data)
    res = create_account_sub(data["reqdata"])
    verify_code_msg(res, data["expdata"])


@pytest.mark.parametrize("data", getdata(data_file, "test_get_observer"))
def test_get_observer(data):
    """获取观察者列表"""
    res = get_observer(data["reqdata"])
    verify_code_msg(res, data["expdata"])


@pytest.mark.parametrize("data", getdata(data_file, "test_create_observer"))
def test_create_observer(data):
    """创建观察者"""
    res = create_observer(data["reqdata"])
    verify_code_msg(res, data["expdata"])


@pytest.mark.parametrize("data", getdata(data_file, "test_create_sub_aggregate"))
def test_create_sub_aggregate(data):
    """创建子账户-聚合
    该接口创建一个子账户和观察者，并设置自动提现地址"""
    # print(data)
    res = create_sub_aggregate(data["reqdata"])
    verify_code_msg(res, data["expdata"])



@pytest.mark.parametrize("data", getdata(data_file, "test_get_account_group"))
def test_get_account_group(data):
    """矿工分组列表"""
    print(data)
    res = get_account_group(data["reqdata"])
    verify_code_msg(res, data["expdata"])


def test_create_account_group():
    """新建矿工分组"""
    data_dev = {'reqdata': {
        "api_key": "",
        "secret_key": "",
        "coin": "BCH",
        "group_name": "group_name1"
    }, 'expdata': {'code': 5007, 'message': 'Worker group exists'}}

    data_pro = {'reqdata': {
        "api_key": "",
        "secret_key": "",
        "coin": "BCH",
        "group_name": "group_name1"
    }, 'expdata': {'code': 5007, 'message': 'Worker group exists'}}
    if settings["env"] != "pro":
        data = data_dev
    else:
        data = data_pro
    res = create_account_group(data["reqdata"])
    verify_code_msg(res, data["expdata"])


def test_put_account_group():
    """移动矿工分组"""
    data_dev = {'reqdata': {
        "api_key": "",
        "secret_key": "",
        "worker_ids": "1753,1795,1796",
        "group_id": 218
    }, 'expdata': {'code': 0, 'message': 'OK'}}
    data_pro = {'reqdata': {
        "api_key": "",
        "secret_key": "",
        "worker_ids": "1753,1795,1796",
        "group_id": 0  # groupid 找不到是会提示非法参数
    }, 'expdata': {'code': 0, 'message': 'OK'}}
    if settings["env"] != "pro":
        data = data_dev
    else:
        data = data_pro
    res = put_account_group(data["reqdata"])
    verify_code_msg(res, data["expdata"])


def test_delete_account_group():
    """删除矿工分组"""
    data_dev = {'reqdata': {
        "api_key": "",
        "secret_key": "",
        "group_id": 219
    }, 'expdata': {'code': 5008, 'message': "Worker group doesn't exist"}}
    data_pro = {'reqdata': {
        "api_key": "",
        "secret_key": "",
        "group_id": 219
    }, 'expdata': {'code': 5008, 'message': "Worker group doesn't exist"}}

    if settings["env"] != "pro":
        data = data_dev
    else:
        data = data_pro
    res = delete_account_group(data["reqdata"])
    verify_code_msg(res, data["expdata"])
