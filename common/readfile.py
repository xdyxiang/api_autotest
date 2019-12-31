# coding=utf8

import yaml,os
from common.config import settings

def read_testdata(file):
    yml = ""
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            yml = yaml.load(content,Loader=yaml.FullLoader)
    except:
        print("读取文件失败！")
    return yml


def getdata(file,data_name):
    data = ""
    try:
        data = read_testdata(file)
        data = data.get(data_name)
    except:
        print("获取数据失败！")
    return data

def get_filepath(filepath):
    path=os.path.split(os.path.realpath(filepath))[0]
    file_name=os.path.split(os.path.realpath(filepath))[1]
    path1 = path.replace("testcase", "datafile")
    if settings["env"] == "pro":
        file_name = file_name.replace(".py", "_pro.yml")
    else:
        file_name = file_name.replace(".py", "_dev.yml")
    file_name1 = file_name.split("test_")[1]
    file_path = os.path.join(path1,file_name1)
    print(file_path)
    return file_path
