import configparser

# 使用相关块
use = "DEFAULT"


def getConfig(option: str, section: str = use):
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')
    return config.get(section, option)
