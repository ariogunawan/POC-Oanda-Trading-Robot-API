# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:43:34 2020

@author: Ario Gunawan
"""
import oanda_login as ol
import requests
import pytz, datetime
import mysql.connector as cn


class kucingTukang():
    @staticmethod
    def strToTime(time, utc):
        timezone = 'Australia/Sydney'
        oanda_time_format = '%Y-%m-%dT%H:%M:%S.000000000Z'
        mysql_time_format = '%Y-%m-%d %H:%M:%S'
        local = pytz.timezone (timezone)
        naive = datetime.datetime.strptime (time, oanda_time_format)
        local_dt = local.localize(naive, is_dst=None)
        utc_dt = local_dt.astimezone(pytz.utc)
        localtime = local_dt.strftime (mysql_time_format)
        utctime = utc_dt.strftime (mysql_time_format)
        return utctime if not(utc is None) and utc.upper() == 'UTC' else localtime    


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
            '/candles?&granularity=' + d_getInstrumentCandles['granularity'] + \
            '&price=' + d_getInstrumentCandles['price_type']
        if not(d_getInstrumentCandles.get('price_from') is None or d_getInstrumentCandles['price_from'] is None):
            url += '&from=' + d_getInstrumentCandles['price_from'].strftime("%Y-%m-%dT%H:%M:%S.000Z")
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        print(endpoint_url)
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

    def getAccountPositions(self):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/positions'
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()

    def getAccountOpenPositions(self):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/openPositions'
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()        

    def getAccountPositionsInstrument(self, d_getAccountPositionsInstrument):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/positions'
        if not(d_getAccountPositionsInstrument.get('instrument') is None or d_getAccountPositionsInstrument['instrument'] is None):
            url += '/' + d_getAccountPositionsInstrument['instrument']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()    

    def getAccountTransactions(self, d_getAccountTransactions):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/transactions'
        if not(d_getAccountTransactions.get('from') is None or d_getAccountTransactions['from'] is None):
            url += '?from=' + d_getAccountTransactions['from']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()

    def getAccountTransactionDetails(self, d_getAccountTransactionDetails):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/transactions'
        if not(d_getAccountTransactionDetails.get('transactionID') is None or d_getAccountTransactionDetails['transactionID'] is None):
            url += '/' + d_getAccountTransactionDetails['transactionID']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()

    def getAccountTransactionRange(self, d_getAccountTransactionRange):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/transactions/idrange'
        if not(d_getAccountTransactionRange.get('from') is None or d_getAccountTransactionRange['from'] is None):
            url += '?from=' + d_getAccountTransactionRange['from'] + \
                '&to=' + d_getAccountTransactionRange['to'] 
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()

    def getAccountTransactionSince(self, d_getAccountTransactionSince):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/transactions'
        if not(d_getAccountTransactionSince.get('id') is None or d_getAccountTransactionSince['id'] is None):
            url += '/sinceid?id=' + d_getAccountTransactionSince['id'] 
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()

    def getAccountLatestCandles(self, d_getAccountLatestCandles):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/candles/latest'
        if not(d_getAccountLatestCandles.get('candleSpecifications') is None or d_getAccountLatestCandles['candleSpecifications'] is None):
            url += '?candleSpecifications=' + d_getAccountLatestCandles['candleSpecifications'] 
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()

    def getAccountPricing(self, d_getAccountPricing):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/pricing'
        if not(d_getAccountPricing.get('instrument') is None or d_getAccountPricing['instrument'] is None):
            url += '?instruments=' + d_getAccountPricing['instrument'] 
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()

    def getAccountInstrumentCandles(self, d_getAccountInstrumentCandles):
        method = 'GET'
        url = '/v3/accounts/' + ol.login.get('account') + \
            '/instruments/' + d_getAccountInstrumentCandles['instrument'] + '/candles'
        if not(d_getAccountInstrumentCandles.get('price') is None or d_getAccountInstrumentCandles['price'] is None):
            url += '?price=' + d_getAccountInstrumentCandles['price'] + \
                '&granularity=' + d_getAccountInstrumentCandles['granularity'] + \
                '&count=' + d_getAccountInstrumentCandles['count']
        endpoint_url = ol.login.get('endpoint_url')
        endpoint_url += url
        r = self.session.request(method, endpoint_url, headers=self.headers)
        return r.json()    
    

class kucingBuku():
    def __init__(self):
        pass

    def updateStatus(self, process_status, comments):
        try:
            conn = cn.connect(user=ol.mysql_login.get('user'), password=ol.mysql_login.get('password'), host=ol.mysql_login.get('host'), database=ol.mysql_login.get('database'))
            mycursor = conn.cursor(buffered=True)

            query = "update system_parameters " \
                    "set process_status = %(process_status)s, comments = %(comments)s"
            d_system_parameters = {}
            d_system_parameters['process_status'] = process_status
            d_system_parameters['comments'] = comments
            mycursor.execute(query, d_system_parameters)
            conn.commit()
            print('Updated Status')
            
        finally:
            mycursor.close()
            conn.close()     

    def raiseError(self, error_message):
        try:
            error_message = (error_message,)
            conn = cn.connect(user=ol.mysql_login.get('user'), password=ol.mysql_login.get('password'), host=ol.mysql_login.get('host'), database=ol.mysql_login.get('database'))
            mycursor = conn.cursor(buffered=True)

            query = "insert into error_log (error_log_message) " \
                    "values (%s)"

            mycursor.execute(query, error_message)
            conn.commit()
            print('Inserted an error message')
            
        finally:
            mycursor.close()
            conn.close()            

    def selectStatus(self):
        try:
            conn = cn.connect(user=ol.mysql_login.get('user'), password=ol.mysql_login.get('password'), host=ol.mysql_login.get('host'), database=ol.mysql_login.get('database'))
            mycursor = conn.cursor(buffered=True, dictionary=True)


            query = "SELECT coalesce(process_status, 'E') as process_status, comments, last_modified " \
                    "FROM system_parameters "
            
            mycursor.execute(query)
            row = mycursor.fetchone()
            
            return row
            
        except:
            print('Something wrong')
            print('Query = ', query)
            
        finally:
            mycursor.close()
            conn.close()            
    
    def insertPrice(self, res):
        try:
            conn = cn.connect(user=ol.mysql_login.get('user'), password=ol.mysql_login.get('password'), host=ol.mysql_login.get('host'), database=ol.mysql_login.get('database'))
            mycursor = conn.cursor(buffered=True)

            query = "insert into price (instrument, granularity, price_type, price_utctime, price_time, complete, volume, open, high, low, close) " \
                    "select %(instrument)s, %(granularity)s, %(price_type)s, %(time_utc)s, %(time)s, %(complete)s, %(volume)s, %(o)s, %(h)s, %(l)s, %(c)s "\
                    "where not exists (select 1 from price p where p.instrument = %(instrument)s and p.granularity = %(granularity)s and p.price_type = %(price_type)s and p.price_time = %(time)s and p.complete = %(complete)s and p.volume = %(volume)s)"
            
            l_candles = []
            for candle in res['candles']:
                if candle['complete'] == True:
                    data = {}
                    data['instrument'] = res.get('instrument')
                    data['granularity'] = res.get('granularity')
                    data['price_type'] = 'mid'
                    data['time_utc'] = kucingTukang.strToTime(candle['time'], 'UTC')
                    data['time'] = kucingTukang.strToTime(candle['time'], None)
                    data['complete'] = candle['complete']
                    data['volume'] = candle['volume']
                    data.update(candle[data['price_type']])
                    l_candles.append(data)
                
            for l_candle in l_candles:
                mycursor.execute(query, l_candle)
                
            conn.commit()
            print('End of Insert Function')
            
        finally:
            mycursor.close()
            conn.close()            
            
    def selectPrice(self):
        try:
            conn = cn.connect(user=ol.mysql_login.get('user'), password=ol.mysql_login.get('password'), host=ol.mysql_login.get('host'), database=ol.mysql_login.get('database'))
            mycursor = conn.cursor(buffered=True, dictionary=True)


            query = "SELECT instrument, granularity, case price_type when 'mid' then 'M' when 'bid' then 'B' else 'A' end as price_type, max(price_utctime) AS price_from " \
                    "FROM price "\
                    "GROUP BY instrument, granularity, price_type"
            
            mycursor.execute(query)
            row = mycursor.fetchone()
            
            return row
            
        except:
            print('Something wrong')
            print('Query = ', query)
            
        finally:
            mycursor.close()
            conn.close()            