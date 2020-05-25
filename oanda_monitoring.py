# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:26:26 2020

@author: Ario Gunawan
"""
from oanda_class import kucingJoget, kucingTukang
from datetime import datetime, timedelta
from urllib.parse import quote, unquote
import mysql.connector as cn

x = kucingJoget()
y = kucingTukang()

# getInstrumentCandles
d_getInstrumentCandles = {
    'instrument' : 'AUD_USD',
    'count' : '2',
    'price' : 'M',
    'granularity' : 'M5',
    'from' : None
    }
#time = datetime(2020, 5, 21, 21, 5, 0, 0)
#time = datetime.now() - timedelta(days=4)
#time = time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
#d_getInstrumentCandles['from'] = quote(time)
res = (x.getInstrumentCandles(d_getInstrumentCandles))

sql = "insert into price (instrument, granularity, price_type, price_utctime, price_localtime, complete, volume, open, high, low, close) " 
sql += "select '" + res['instrument'] + "', '" + res['granularity'] + "', '" + "mid" + "', '" + y.strToTime(res['candles'][0]['time'], 'UTC') + "', '" 
sql += y.strToTime(res['candles'][0]['time'], None) + "', '" + str(res['candles'][0]['complete']) + "', " + str(res['candles'][0]['volume']) + ", " 
sql += str(res['candles'][0]['mid']['o']) + ", " + str(res['candles'][0]['mid']['h']) + ", " + str(res['candles'][0]['mid']['l']) + ", " + str(res['candles'][0]['mid']['c'])

print(sql)

cnx = cn.connect(user='root', password='kucingjoget',
                              host='localhost',
                              database='oanda')

mycursor = cnx.cursor()
# INSERT ROW
mycursor.execute(sql)
cnx.commit()
print(mycursor.rowcount, " records inserted")

# SELECT ROW
#mycursor.execute("select * from price")
#res = mycursor.fetchall()
cnx.close()
