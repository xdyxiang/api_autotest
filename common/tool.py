# coding=utf8
import hmac
from hashlib import sha256
import time
from .config import *


def get_time_stamp():
    stamp = round(time.time() * 1000)
    return stamp


def hash_encrypt(secret_key, query_string):
    secret_key = bytes(secret_key, encoding="utf-8")
    query_string = bytes(query_string, encoding="utf-8")
    sign = hmac.new(secret_key, query_string, sha256).hexdigest()
    return sign


def get_baseurl(project="pool"):
    if project == "pool":
        if settings["env"] == "pro":
            base_url = base_url_pro
        elif settings["env"] == "dev1":
            base_url = base_url_dev1
        elif settings["env"] == "dev2":
            base_url = base_url_dev2
        elif settings["env"] == "dev3":
            base_url = base_url_dev3
        else:
            base_url = base_url_dev1

        return base_url

    if  project == "wallet":
        if settings["env"] == "dev":
            wallet_base_url = wallet_url_dev
        elif settings["env"] == "pro":
            wallet_base_url = wallet_url_pro
        else:
            wallet_base_url = wallet_url_dev

        return wallet_base_url
