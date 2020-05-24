# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:43:34 2020

@author: Ario Gunawan
"""
import oanda_login as ol
import requests

class kucingJoget():
    def __init__(self):
        self.session = requests.Session()
        self.headers = ol.headers

    def getAccountId(self):
        method = 'GET'
        url = '/v3/accounts'
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()
    
    def getAccountDetails(self):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account')
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()    

    def getAccountSummary(self):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + '/summary'
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()    
    
    def getAccountInstrument(self, d_getAccountInstrument):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + '/instruments'
        if not(d_getAccountInstrument.get('instrument') is None or d_getAccountInstrument['instrument'] is None):
            url += '?instruments=' + d_getAccountInstrument['instrument']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()       
    
    def getAccountChange(self, d_getAccountChange):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + '/changes'
        if not(d_getAccountChange.get('sinceTransactionID') is None or d_getAccountChange['sinceTransactionID'] is None):
            url += '?sinceTransactionID=' + \
                d_getAccountChange['sinceTransactionID']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()           

    def getInstrumentCandles(self, d_getInstrumentCandles):
        method = 'GET'
        url = '/v3/instruments/' + d_getInstrumentCandles['instrument'] + \
            '/candles?count=' + d_getInstrumentCandles['count'] + \
            '&price=' + d_getInstrumentCandles['price'] + \
            '&granularity=' + d_getInstrumentCandles['granularity']
        if not(d_getInstrumentCandles.get('from') is None or d_getInstrumentCandles['from'] is None):
            url += '&from=' + d_getInstrumentCandles['from']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()

    def getInstrumentOrderBook(self, d_getInstrumentOrderBook):
        method = 'GET'
        url = '/v3/instruments/' + d_getInstrumentOrderBook['instrument'] + \
            '/orderBook'
        if not(d_getInstrumentOrderBook.get('time') is None or d_getInstrumentOrderBook['time'] is None):
            url += '?time=' + d_getInstrumentOrderBook['time']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()
    
    def getInstrumentPositionBook(self, d_getInstrumentPositionBook):
        method = 'GET'
        url = '/v3/instruments/' + d_getInstrumentPositionBook['instrument'] + \
            '/positionBook'
        if not(d_getInstrumentPositionBook.get('time') is None or d_getInstrumentPositionBook['time'] is None):
            url += '?time=' + d_getInstrumentPositionBook['time']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()
    
    def getAccountOrders(self, d_getAccountOrders):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/orders'
        if not(d_getAccountOrders.get('count') is None or d_getAccountOrders['count'] is None):
            url += '?count=' + d_getAccountOrders['count']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()

    def getAccountPendingOrders(self):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/pendingOrders'
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()        

    def getAccountOrderDetails(self, d_getAccountOrderDetails):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/orders'
        if not(d_getAccountOrderDetails.get('orderSpecifier') is None or d_getAccountOrderDetails['orderSpecifier'] is None):
            url += '/' + d_getAccountOrderDetails['orderSpecifier']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()    
#
    def getAccountTrades(self, d_getAccountTrades):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/trades'
        if not(d_getAccountTrades.get('count') is None or d_getAccountTrades['count'] is None):
            url += '?count=' + d_getAccountTrades['count']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()

    def getAccountOpenTrades(self):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/openTrades'
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()        

    def getAccountTradeDetails(self, d_getAccountTradeDetails):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/trades'
        if not(d_getAccountTradeDetails.get('tradeSpecifier') is None or d_getAccountTradeDetails['tradeSpecifier'] is None):
            url += '/' + d_getAccountTradeDetails['tradeSpecifier']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()    
    