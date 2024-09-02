# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:41:43 2020

@author: Ario Gunawan
"""
login = {
    'api_key' : '',
    'account' : '',
    'endpoint_url' : 'https://api-fxpractice.oanda.com'
}

headers = {
    'Content-Type' : 'application/json',
    'Accept-Datetime-Format' : 'RFC3339'
}

headers['Authorization'] = 'Bearer' + ' ' + login.get('api_key')

mysql_login = {
    'user' : '',
    'password' : '',
    'host' : '',#'198.199.74.158',
    'database' : 'oanda'
    }
