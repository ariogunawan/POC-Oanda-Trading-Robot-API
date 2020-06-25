# -*- coding: utf-8 -*-
from oanda_class import kucingJoget

trade = kucingJoget()

data = {
    'order':
        {'units': '100', 'instrument': 'EUR_USD', 'timeInForce': 'FOK', 'type': 'MARKET', 'positionFill': 'DEFAULT',
         'stopLossOnFill':
             {
                 'timeInForce': 'GTC',
                 'price': '1.1200'
             },
         'takeProfitOnFill':
             {
                 'price': '1.1300'
             }
         }
}
# print(trade.createAccountOrder(data))
update = {
    'takeProfit': {
        'timeInForce': 'GTC',
        'price': '1.1310'
    },
    'stopLoss': {
        'timeInForce': 'GTC',
        'price': '1.1210'
    }
}
print(trade.replaceAccountOrder(update, '129'))
