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
        if not(d_getAccountInstrument['instrument'] is None):
            url += '?instruments=' + d_getAccountInstrument['instrument']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()       
    
    def getAccountChange(self, d_getAccountChange):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + '/changes'
        if not(d_getAccountChange['sinceTransactionID'] is None):
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
        if not(d_getInstrumentCandles['from'] is None):
            url += '&from=' + d_getInstrumentCandles['from']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()

    def getInstrumentOrderBook(self, d_getInstrumentOrderBook):
        method = 'GET'
        url = '/v3/instruments/' + d_getInstrumentOrderBook['instrument'] + \
            '/orderBook'
        if not(d_getInstrumentOrderBook['time'] is None):
            url += '?time=' + d_getInstrumentOrderBook['time']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()
    
    def getInstrumentPositionBook(self, d_getInstrumentPositionBook):
        method = 'GET'
        url = '/v3/instruments/' + d_getInstrumentPositionBook['instrument'] + \
            '/positionBook'
        if not(d_getInstrumentPositionBook['time'] is None):
            url += '?time=' + d_getInstrumentPositionBook['time']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()    