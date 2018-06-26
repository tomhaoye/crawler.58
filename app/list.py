import logging
import requests
from util.orm import Session
from model import Area
import config
import json
from model.community import Community

db_session = Session()


def fetch_list_pages(db, city_index):
    logging.info('抓取区域列表')
    areas_obj = db.query(Area).filter(
        Area.city_index == city_index,
        Area.insert == 0
    ).all()
    for area in areas_obj:
        page = 1
        while True:
            logging.info(f'正在抓取第{page}页')
            api_url = f'http://m.58.com/xiaoquweb/getXiaoquList/?city={area.area_index}&page={page}'
            res = requests.get(api_url, headers=config.config.headers, timeout=5)
            res.raise_for_status()
            res_json_obj = json.loads(res.content)
            if res_json_obj['code'] == "0":
                page_dto = res_json_obj['data']['pageDTO']
                info_list = res_json_obj['data']['infoList']
                if page_dto['currentPageNo'] > page_dto['totalPage']:
                    break
                for community in info_list:
                    add_community = Community(city_index, area.area_index, community)
                    db.add(add_community)
                    logging.info('新增1条小区信息')
            page += 1
        area.insert = 1
        db.commit()

    logging.info('抓取区域列表数据完毕')
    db.close()


def main(city_index):
    fetch_list_pages(db_session, city_index)


if __name__ == '__main__':
    main(config.config.city_index)
