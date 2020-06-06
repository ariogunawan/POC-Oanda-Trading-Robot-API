# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:26:26 2020

@author: Ario Gunawan
"""
from oanda_class import kucingJoget, kucingTukang, kucingBuku

x = kucingJoget()
z = kucingBuku()

# Check if there's a current batch running
d_batch_status = z.selectAction('batch status')
if d_batch_status['action_value'] == 'R' or d_batch_status['action_value'] == 'E':
    print('Batch is currently running or was halted!')
    exit()
elif d_batch_status['action_value'] == 'C':
    # Set status as 'R' Running
    z.updateAction('batch status', 'R', None)    
    
    d_batch_status = z.selectAction('update price')
    if d_batch_status['action_value'] == 'Y':
        # Load the latest price_utctime, feed the result into a dictionary
        d_getInstrumentCandles = z.selectPrice()
        
        # Get the latest candles SINCE the latest price_utctime in the database
        res = (x.getInstrumentCandles(d_getInstrumentCandles))
        
        # Insert the latest candles SINCE the latest price_utctime in the database
        z.insertPrice(res)
        
        # perform calculation on SMA, Stochastic
        z.updateIndicator(d_getInstrumentCandles, 'all')

    # Set status as 'C' Completed
    z.updateAction('batch status', 'C', None)
    print('Batch run completed')
else:
    # insert unknown error, set to E
    z.updateAction('batch status', 'E', 'Error in retrieving batch status')
    print('Batch status retrieval error')

    
