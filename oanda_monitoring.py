# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:26:26 2020

@author: Ario Gunawan
"""
from oanda_class import kucingJoget, kucingTukang, kucingBuku
from datetime import datetime, timedelta
from urllib.parse import quote, unquote
import mysql.connector as cn

x = kucingJoget()
z = kucingBuku()

# getInstrumentCandles
d_getInstrumentCandles = {
    'instrument' : 'AUD_USD',
    'count' : '10',
    'price' : 'M',
    'granularity' : 'M5',
    'from' : None
    }
#time = datetime(2020, 5, 21, 21, 5, 0, 0)
#time = datetime.now() - timedelta(days=4)
#time = time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
#d_getInstrumentCandles['from'] = quote(time)
res = (x.getInstrumentCandles(d_getInstrumentCandles))

# loadPrice - check the latest price time for the instrument
# then call res FROM latest price time

z.insertPrice(res)
