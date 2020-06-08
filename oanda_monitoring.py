# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:26:26 2020

@author: Ario Gunawan
"""
from sys import exit
from oanda_class import kucingJoget, kucingBuku

x = kucingJoget()
z = kucingBuku()

# BATCH RUN SECTION
d_action_list = z.selectAction('batch status')
if d_action_list['action_value'] == 'R' or d_action_list['action_value'] == 'E':
    print('Batch is currently running or was halted!')
    exit()
elif d_action_list['action_value'] == 'C':
    # Set status as 'R' Running
    z.updateAction('batch status', 'R', None)    
    
    # PRICE SECTION    
    d_action_list = z.selectAction('update price')
    if d_action_list['action_value'] == 'Y':
        # Load the latest price_utctime, feed the result into a dictionary
        d_getInstrumentCandles = z.selectPrice()
        # Get the latest candles SINCE the latest price_utctime in the database
        res = (x.getInstrumentCandles(d_getInstrumentCandles))
        # Insert the latest candles SINCE the latest price_utctime in the database
        z.insertPrice(res)
    # END PRICE SECTION
    
    # INDICATOR SECTION
    d_action_list = z.selectAction('update indicator')
    if d_action_list['action_value'] == 'Y':
        # perform calculation on SMA, Stochastic
        z.updateIndicator(d_getInstrumentCandles, d_action_list['action_message'])
    # END INDICATOR SECTION

    # check balance
    d_getAccountSummary = x.getAccountSummary()
    d_accountSummary = d_getAccountSummary.get('account')
    #print(d_getAccountSummary)
    
    # check how many open positions
    
    # rules validation
    # balance ok, position safe, formula good, enter
        
    # CLEANUP SECTION
    d_action_list = z.selectAction('truncate old data')
    if d_action_list['action_value'] == 'Y':
        z.deletePrice(d_action_list['action_message'])
    # END CLEANUP SECTION
    
# END BATCH COMPLETED
    z.updateAction('batch status', 'C', None)
else:
    # insert unknown error, set to E
    z.updateAction('batch status', 'E', 'Error in retrieving batch status')
    print('Batch status retrieval error')