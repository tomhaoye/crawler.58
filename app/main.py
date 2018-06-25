import logging
from pathlib import Path
from model import Area
from util.orm import Session
from pyquery import PyQuery
import requests
import config


DATA_DIR = Path(__file__).parent.joinpath('../html/area/').resolve()
DATA_DIR.mkdir(parents=True, exist_ok=True)
db_session = Session()


def insert_db_area(db, city_index, area_index, area_id):
    exist = db.query(Area).filter(
        Area.city_index == city_index,
        Area.area_index == area_index,
    ).first()
    if not exist:
        area = Area(city_index, area_index, area_id)
        db.add(area)
        db.commit()
        logging.info('新增1条区域信息')


def fetch_page(city_name):
    logging.info('抓取页面中')
    url = f'http://{city_name}.58.com/xiaoqu/'
    res = requests.get(url)
    res.raise_for_status()

    save_file = DATA_DIR.joinpath(f'{city_name}.html')
    save_file.write_bytes(res.content)
    logging.info('抓取页面完成')


def analyze(db, city_name):
    logging.info('分析区域与数据入库中')
    doc = PyQuery(DATA_DIR.joinpath(f'{city_name}.html').read_text(encoding='utf-8'))
    areas = doc('.quyu')
    while areas:
        area_id = areas.attr.id
        area_index = areas.attr.listname
        areas = areas.next()
        if area_index is not None:
            insert_db_area(db, city_name, area_index, area_id)
    logging.info('分析区域与数据入库done')
    db.close()


def main(city_name):
    fetch_page(city_name)
    analyze(db_session, city_name)


if __name__ == '__main__':
    main(config.config.city_index)
