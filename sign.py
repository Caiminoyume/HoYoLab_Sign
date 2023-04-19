import json
import os
import time

import requests
import schedule

from log import log

if not os.path.exists('./config'):
    os.mkdir('./config')
with open('./config/cookies.txt', 'r') as f:
    cookies = [cookie for cookie in f.readlines()]
OS_SIGN_URL = 'https://hk4e-api-os.mihoyo.com/event/sol/sign?lang=zh-cn'
OS_REFERER_URL = 'https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481'
data = {
    'act_id': 'e202102251931481'
}


def sign():
    log.info('开始签到！')
    for cookie in cookies:
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E150',
            'Referer': OS_REFERER_URL,
            'Accept-Encoding': 'gzip, deflate, br',
            'Cookie': cookie
        }
        response = requests.post(url=OS_SIGN_URL,
                                 data=json.dumps(data, ensure_ascii=False),
                                 headers=headers)
        if response.status_code == 200:
            log.info('签到完成！')
        else:
            log.warning('签到失败！')


def run():
    schedule.every().day.at("06:30").do(sign)
    log.info('启动完成')
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    run()
