import time
import config
import requests


def get_data(url, payload, method='GET'):
    payload['request_ts'] = int(time.time())

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    }

    func = requests.get if method == 'GET' else requests.post
    return func(url, payload, headers=headers)
