# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:26:26 2020

@author: Ario Gunawan
"""
from oanda_class import kucingJoget
from datetime import datetime, timedelta
from urllib.parse import quote, unquote

x = kucingJoget()

## getAccountId
#print(x.getAccountId())

## getAccountInstrument
d_getAccountInstrument = {
    'instrument' : 'USD_JPY'
    }
#print(x.getAccountInstrument(d_getAccountInstrument))

## getAccountChange
d_getAccountChange = {
    'sinceTransactionID': '42'
    }
#print(x.getAccountChange(d_getAccountChange))

## getInstrumentCandles
d_getInstrumentCandles = {
    'instrument' : 'USD_JPY',
    'count' : '2',
    'price' : 'M',
    'granularity' : 'M5',
    'from' : None
    }
time = datetime(2020, 5, 21, 21, 5, 0, 0)
time = datetime.now() - timedelta(days=4)
time = time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
d_getInstrumentCandles['from'] = quote(time)
#print(x.getInstrumentCandles(d_getInstrumentCandles))

## getInstrumentOrderBook
d_getInstrumentOrderBook = {
    'instrument' : 'USD_JPY',
    'time' : None
    }
#time = datetime.now() - timedelta(days=4)
time = datetime(2020, 5, 21, 21, 0, 0, 0)
time = time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
d_getInstrumentOrderBook['time'] = quote(time)
#print(x.getInstrumentOrderBook(d_getInstrumentOrderBook))

## getInstrumentPositionBook
d_getInstrumentPositionBook = {
    'instrument' : 'USD_JPY',
    'time' : None  #'time': '2020-05-19T13:00:00.000Z' #hourly only!
    }
time = datetime(2020, 5, 21, 21, 0, 0, 0)
time = time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
d_getInstrumentPositionBook['time'] = quote(time)
#print(x.getInstrumentPositionBook(d_getInstrumentPositionBook))
