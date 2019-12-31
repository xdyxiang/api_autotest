# coding=utf-8

def verify_code_msg(res,expdata):
    assert res["code"] == expdata["code"]
    assert res["message"] == expdata["message"]
