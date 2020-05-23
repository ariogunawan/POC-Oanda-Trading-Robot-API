# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:26:26 2020

@author: Ario Gunawan
"""
from oanda_class import kucingJoget

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
    'granularity' : 'M5'
    }
print(x.getInstrumentCandles(d_getInstrumentCandles))

