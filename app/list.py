import logging
import requests
from pathlib import Path
from util.orm import Session
from model import Area
from pyquery import PyQuery
import config
import time
from proxy import gen_proxies
import random
import json
from model.community import Community

DATA_DIR = Path(__file__).parent.joinpath('../html/list/').resolve()
DATA_DIR.mkdir(parents=True, exist_ok=True)

proxy = gen_proxies()
db_session = Session()


def fetch_list_pages(db, city_index):
    logging.info('抓取区域列表')
    areas_obj = db.query(Area).filter(
        Area.city_index == city_index,
        Area.insert == 0
    ).all()
    for area in areas_obj:
        page = 1
        # proxies = next(proxy)
        # logging.info(f'代理:{proxies}')
        while True:
            logging.info(f'正在抓取第{page}页')

            # url = f'http://{city_index}.58.com/xiaoqu/{area.area_index}/pn_{page}/'

            api_url = f'http://m.58.com/xiaoquweb/getXiaoquList/?city={area.area_index}&page={page}'
            res = requests.get(api_url, headers=config.config.headers, timeout=5)
            res.raise_for_status()
            res_json_obj = json.loads(res.content)
            if res_json_obj['code'] == "0":
                page_dto = res_json_obj['data']['pageDTO']
                list = res_json_obj['data']['infoList']
                if page_dto['currentPageNo'] > page_dto['totalPage']:
                    break
                for community in list:
                    add_community = Community(city_index, area.area_index, community)
                    db.add(add_community)
                    logging.info('新增1条小区信息')
                db.commit()

            # save_file = DATA_DIR.joinpath(f'{city_index}_{area.area_index}_{page}.html')
            # save_file.write_bytes(res.content)
            # doc = PyQuery(res.content)
            # tbody_list = doc('#infolist tbody')

            page += 1
            # time.sleep(random.randint(1, 2))

            # if tbody_list.text() == '':
            #     logging.warning('页面数据为空，该区域抓取完毕或被限制访问')
            #     break
        area.insert = 1
        db.commit()

    logging.info('抓取区域列表数据完毕')
    db.close()


def main(city_index):
    fetch_list_pages(db_session, city_index)


if __name__ == '__main__':
    main(config.config.city_index)
