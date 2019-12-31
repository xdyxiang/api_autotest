# coding=utf8

from verify_response.verify_base import verify_code_msg
from api_request.openapi.hashrate_api import *
import pytest
from common.readfile import get_filepath, getdata


data_file = get_filepath(__file__)

@pytest.mark.parametrize("data", getdata(data_file, "test_get_hashrate"))
def test_get_hashrate(data):
    """获取账户实时算力"""
    res = get_hashrate(data["reqdata"])
    verify_code_msg(res, data["expdata"])


@pytest.mark.parametrize("data", getdata(data_file, "test_get_hashrate_history"))
def test_get_hashrate_history(data):
    """获取账户历史算力"""
    res = get_hashrate_history(data["reqdata"])
    verify_code_msg(res, data["expdata"])


@pytest.mark.parametrize("data", getdata(data_file, "test_get_hashrate_chart"))
def test_get_hashrate_chart(data):
    """获取账户算力曲线"""
    res = get_hashrate_chart(data["reqdata"])
    verify_code_msg(res, data["expdata"])


@pytest.mark.parametrize("data", getdata(data_file, "test_get_hashrate_worker"))
def test_get_hashrate_worker(data):
    """获取矿工实时算力"""
    res = get_hashrate_worker(data["reqdata"])
    verify_code_msg(res, data["expdata"])


@pytest.mark.parametrize("data", getdata(data_file, "test_get_hashrate_worker_single"))
def test_get_hashrate_worker_single(data):
    """获取单个矿工实时算力"""
    res = get_hashrate_worker_single(data["reqdata"])
    verify_code_msg(res, data["expdata"])


@pytest.mark.parametrize("data", getdata(data_file, "test_get_hashrate_worker_history"))
def test_get_hashrate_worker_history(data):
    """获取矿工历史算力"""
    res = get_hashrate_worker_history(data["reqdata"])
    verify_code_msg(res, data["expdata"])


@pytest.mark.parametrize("data", getdata(data_file, "test_get_hashrate_group"))
def test_get_hashrate_group(data):
    """获取分组实时算力"""
    res = get_hashrate_group(data["reqdata"])
    verify_code_msg(res, data["expdata"])

@pytest.mark.parametrize("data", getdata(data_file, "test_get_hashrate_group_single"))
def test_get_hashrate_group_single(data):
    """获取单个分组实时算力"""
    res = get_hashrate_group_single(data["reqdata"])
    verify_code_msg(res, data["expdata"])
