import config
from util.orm import Session
from model.community import Community
import requests
import logging
from pyquery import PyQuery
import json

db_session = Session()


def fetch_detail_page(db, city_index):
    communities = db.query(Community).filter(
        Community.city_index == city_index,
        Community.detail_info == None
    ).all()
    for community in communities:
        logging.info(f'开始抓取{community.alias}小区详情页数据')
        url = f'http://m.58.com/xiaoqu/{community.listname}/'
        try:
            res = requests.get(url, headers=config.config.headers, timeout=5)
            res.raise_for_status()
        except Exception as e:
            logging.error(f' 错误信息: {e}')
            continue
        doc = PyQuery(res.content)
        keys = []
        values = []
        keys_values = doc('.xq-info .info-con span')
        index = 0
        for kv in keys_values:
            if index % 2 == 0:
                keys.append(kv.text.strip(':'))
            else:
                values.append(kv.text)
            index += 1
        detail_json = dict(zip(keys, values))
        scripts_info = doc('script')
        for script in scripts_info:
            if 'lat:' in script.text:
                step_one = script.text.split('lat: \'')[1]
                lat = step_one.split('\', lon: \'')[0]
                lon = step_one.split('\', lon: \'')[1].split('\' }')[0]
                community.lat_lon = f'{lat},{lon}'
                break
        community.detail_info = json.dumps(detail_json, ensure_ascii=False)
        if community.alias == '':
            alias = doc('.xq-basic .name').text()
            community.alias = alias
        db.commit()
        logging.info(f'抓取{community.alias}小区数据完成')
        # time.sleep(1)
    logging.info(f'抓取{city_index}所有小区数据完成')
    db.close()


def main(city_index):
    fetch_detail_page(db_session, city_index)


if __name__ == '__main__':
    main(config.config.city_index)
