# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:41:43 2020

@author: Ario Gunawan
"""
login = {
    'api_key': 'bb0b5987ddb4ae39ff364ad45c7377bc-8dc59ab8f6656357f8de1db5929b54c3',
    'account': '101-011-13344081-001',
    'endpoint_url': 'https://api-fxpractice.oanda.com'
}

headers = {
    'Content-Type': 'application/json'
}

headers['Authorization'] = 'Bearer' + ' ' + login.get('api_key')