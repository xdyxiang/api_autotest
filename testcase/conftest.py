# coding=utf8

from common.config import settings

# 接收一个env命令行参数
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="", help="By default: dev. you can chose pro")

# 把命令行参数赋值到配置文件的setting
def pytest_configure(config):
    if config.getoption('--env'):
        settings["env"] = config.getoption('--env')
    print(settings["env"])
