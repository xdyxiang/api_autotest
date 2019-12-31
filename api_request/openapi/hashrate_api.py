# coding=utf8

from common.send_func import send_get
from common.tool import get_baseurl



base_url = get_baseurl()


def get_hashrate(data):
    """获取账户实时算力"""
    api_key = data["api_key"]
    coin = data["coin"]
    param = {
        "coin": coin
    }
    url = base_url + "openapi/v1/hashrate"
    header = {
        "X-API-KEY": api_key
    }
    res = send_get(url, param, header)
    return res


def get_hashrate_history(data):
    """获取账户历史算力"""
    api_key = data["api_key"]
    coin = data["coin"]
    start_date = data["start_date"]  # 2019-01-28
    end_date = data["end_date"]
    utc = data["utc"]
    page = data["page"]
    limit = data["limit"]

    param = {
        "coin": coin,
        "start_date": start_date,  # 2019-01-24
        "end_date": end_date,
        "utc": utc,
        "page": page,
        "limit": limit
    }
    url = base_url + "openapi/v1/hashrate/history"
    header = {
        "X-API-KEY": api_key
    }
    res = send_get(url, param, header)
    return res


def get_hashrate_chart(data):
    """获取账户算力曲线"""
    api_key = data["api_key"]
    coin = data["coin"]
    interval = data["interval"]
    period = data["period"]
    utc = data["utc"]
    param = {
        "coin": coin,
        "interval": interval,  # min/hour/day，取样点间隔，每10分钟/1小时/1天
        "period": period, # 点数量
        "utc": utc  # 仅interval=day时有效
    }
    url = base_url + "openapi/v1/hashrate/chart"
    header = {
        "X-API-KEY": api_key
    }
    res = send_get(url, param, header)
    return res


def get_hashrate_worker(data):
    """获取矿工实时算力"""
    api_key = data["api_key"]
    coin = data["coin"]
    group_id = data["group_id"]
    worker_status = data["worker_status"]
    page = data["page"]
    limit = data["limit"]
    param = {
        "coin": coin,
        "group_id": group_id,
        "worker_status": worker_status,
        "page": page,
        "limit": limit
    }
    url = base_url + "openapi/v1/hashrate/worker"
    header = {
        "X-API-KEY": api_key
    }
    res = send_get(url, param, header)
    return res


def get_hashrate_worker_single(data):
    """获取单个矿工实时算力"""
    api_key = data["api_key"]
    worker_id = data["worker_id"]
    url = base_url + "openapi/v1/hashrate/worker/{0}".format(worker_id)
    param = None
    header = {
        "X-API-KEY": api_key
    }
    res = send_get(url, param, header)
    return res


def get_hashrate_worker_history(data):
    """获取矿工历史算力"""
    api_key = data["api_key"]
    worker_id = data["worker_id"]
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
    url = base_url + "openapi/v1/hashrate/worker/{0}/history".format(worker_id)
    header = {
        "X-API-KEY": api_key
    }
    res = send_get(url, param, header)
    return res


def get_hashrate_group(data):
    """获取分组实时算力"""
    api_key = data["api_key"]
    coin = data["coin"]
    page = data["page"]
    limit = data["limit"]
    param = {
        "coin": coin,
        "page": page,
        "limit": limit
    }
    url = base_url + "openapi/v1/hashrate/group"
    header = {
        "X-API-KEY": api_key
    }
    res = send_get(url, param, header)
    return res


def get_hashrate_group_single(data):
    """获取单个分组实时算力"""
    api_key = data["api_key"]
    group_id = data["group_id"]
    url = base_url + "openapi/v1/hashrate/group/{0}".format(group_id)
    param = None
    header = {
        "X-API-KEY": api_key
    }
    res = send_get(url, param, header)
    return res
