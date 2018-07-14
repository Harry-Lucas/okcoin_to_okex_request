#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
from threading import Timer

#初始化apikey，secretkey,url
apikey = ''
secretkey = ''
okcoinRESTURL = 'https://www.okex.com'   #请求注意：国内账号需要 修改为 www.okcoin.cn,

#现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)

#期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL,apikey,secretkey)

def get_future_index():
    print(u' 现货行情 ', okcoinSpot.ticker('btc_usd')['future_index'])
    Timer(1, get_future_index).start()

def get_future_data():
    print(u' 期货行情', okcoinFuture.future_ticker('btc_usd', 'this_week')['ticker']['last'])
    Timer(1, get_future_data).start()

if __name__ == '__main__':
    threads = []
    threads.append(Timer(0, get_future_index))
    threads.append(Timer(0, get_future_data))
    for i in threads:
        i.start()


