import requests
import schedule
import json
import time

from log import log


OS_SIGN_URL = 'https://hk4e-api-os.mihoyo.com/event/sol/sign?lang=zh-cn'
OS_REFERER_URL = 'https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481'
cookie = 'mi18nLang=zh-cn; _MHYUUID=be9dd390-bb15-4fd1-8c53-f6f5afe042c4; _ga=GA1.1.214606768.1674386087; DEVICEFP_SEED_ID=c9b1d310262f6cbf; DEVICEFP_SEED_TIME=1674386087281; ltoken=begl13G4sDb1TUiCL2sekeZRPC1g0jx23XTA33ij; ltuid=111768572; _ga_JRFG0HQ22J=GS1.1.1674386087.1.1.1674386292.0.0.0; DEVICEFP=38d7eccea1582; _ga_54PBK3QDF4=GS1.1.1680409969.4.1.1680411818.0.0.0'
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E150',
    'Referer': OS_REFERER_URL,
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': cookie
}
data = {
    'act_id': 'e202102251931481'
}


def sign():
    log.info('开始签到！')
    response = requests.post(url=OS_SIGN_URL,
                             data=json.dumps(data, ensure_ascii=False),
                             headers=headers)
    if response.status_code == 200:
        log.info('签到完成！')
    else:
        log.warning('签到失败！')


def run():
    schedule.every().day.at("06:30").do(sign)
    print('启动完成')
    log.info('启动完成')
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    run()
