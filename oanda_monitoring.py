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
# Load the latest price_utctime, feed the result into a dictionary
d_getInstrumentCandles = z.selectPrice()

# Get the latest candles SINCE the latest price_utctime in the database
res = (x.getInstrumentCandles(d_getInstrumentCandles))

# Insert the latest candles SINCE the latest price_utctime in the database
z.insertPrice(res)

# perform calculation on SMA, Stochastic
