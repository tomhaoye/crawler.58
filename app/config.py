import logging
import sys
from pathlib import Path
import json

logging.basicConfig(format='%(asctime)s %(name)s[%(module)s] %(levelname)s: %(message)s', level=logging.INFO)
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "AlexaToolbar-ALX_NS_PH": "AlexaToolbar/alx-4.0.3",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "m.58.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}


class Config:
    def __init__(self):
        self.city_index = 'gz'
        self.headers = {}
        self.database = {}


def load():
    this_config = Config()
    if len(sys.argv) < 2:
        logging.warning('沒有输入城市代号，默认使用gz')
    else:
        this_config.city_index = sys.argv[1]
        this_config.headers = headers

    config_name = 'config.example.json'
    logging.info(f'配置文件 "{config_name}"')
    config_file = Path(__file__).parent.joinpath(config_name)
    if not config_file.exists():
        sys.exit(f'配置文件{config_name}不存在')
    config_json = config_file.resolve()
    config_dict = json.loads(config_json.read_text())
    this_config.database = config_dict['database']

    return this_config


config = load()
