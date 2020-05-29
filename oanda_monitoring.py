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

# Check if there's a current batch running
d_system_parameters = z.selectStatus()
if d_system_parameters['process_status'] == 'E' or d_system_parameters['process_status'] == 'R' or d_system_parameters['process_status'] == 'S' :
    exit()
elif d_system_parameters['process_status'] == 'C':
    # Set status as 'R' Running
    z.updateStatus('R', 'Process is running')    
    
    # Load the latest price_utctime, feed the result into a dictionary
    d_getInstrumentCandles = z.selectPrice()
    
    # Get the latest candles SINCE the latest price_utctime in the database
    res = (x.getInstrumentCandles(d_getInstrumentCandles))
    
    # Insert the latest candles SINCE the latest price_utctime in the database
    z.insertPrice(res)
    
    # perform calculation on SMA, Stochastic
    
    # Set status as 'C' Completed
    z.updateStatus('C', 'Process completed')        
else:
    # insert unknown error, set to E
    error_message = 'Unknown error: system_parameters.process_status = ' + d_system_parameters['process_status']
    z.raiseError(error_message)
    z.updateStatus('E', error_message)

    
