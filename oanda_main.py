# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:26:26 2020

@author: Ario Gunawan
"""
from oanda_class import kucingJoget, kucingTukang
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
print(x.getInstrumentCandles(d_getInstrumentCandles))

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

## getAccountOrders
d_getAccountOrders = {}
#print(x.getAccountOrders(d_getAccountOrders))

## getAccountPendingOrders
#print(x.getAccountPendingOrders())

## getAccountOrderDetails
d_getAccountOrderDetails = {'orderSpecifier' : None}
#print(x.getAccountOrderDetails(d_getAccountOrderDetails))

## getAccountTrades
d_getAccountTrades = {}
#print(x.getAccountTrades(d_getAccountTrades))

## getAccountOpenTrades
#print(x.getAccountOpenTrades())

## getAccountTradeDetails
d_getAccountTradeDetails = {'tradeSpecifier' : None}
#print(x.getAccountTradeDetails(d_getAccountTradeDetails))

## getAccountPositions
#print(x.getAccountPositions())

## getAccountOpenPositions
#print(x.getAccountOpenPositions())

## getAccountPositionsInstrument
d_getAccountPositionsInstrument = {'instrument' : 'USD_JPY'}
#print(x.getAccountPositionsInstrument(d_getAccountPositionsInstrument))

## getAccountTransactions
d_getAccountTransactions = {'from' : None}
time = datetime(2020, 5, 21, 21, 0, 0, 0)
time = time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
d_getAccountTransactions['from'] = quote(time)
#print(x.getAccountTransactions(d_getAccountTransactions))

## getAccountTransactionDetails
d_getAccountTransactionDetails = {'transactionID' : None}
#print(x.getAccountTransactionDetails(d_getAccountTransactionDetails))

## getAccountTransactionRange
d_getAccountTransactionRange = {'from' : '42', 'to' : '42'}
#print(x.getAccountTransactionRange(d_getAccountTransactionRange))

## getAccountTransactionSince
d_getAccountTransactionSince = {'id' : '42'}
#print(x.getAccountTransactionSince(d_getAccountTransactionSince))

## getAccountLatestCandles
d_getAccountLatestCandles = {'candleSpecifications' : 'AUD_USD:M5:M'}
#print(x.getAccountLatestCandles(d_getAccountLatestCandles))

## getAccountPricing
d_getAccountPricing = {'instrument' : 'AUD_USD'}
#print(x.getAccountPricing(d_getAccountPricing))

## getAccountInstrumentCandles
d_getAccountInstrumentCandles = {'instrument' : 'AUD_USD', 'price' : 'M', 'granularity' : 'M5', 'count' : '2'}
print(x.getAccountInstrumentCandles(d_getAccountInstrumentCandles))


## WHATS NEXT
# mysql insert

## BACKLOG
# getAccountTransactionStream # streaming endpoint
# getAccountPricingStream  # streaming endpoint
