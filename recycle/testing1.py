
# d_AccountSummary = {'account': {'guaranteedStopLossOrderMode': 'DISABLED', 'hedgingEnabled': False, 'id': '101-011-13344081-001', 'createdTime': '2020-02-03T10:38:42.866028837Z', 'currency': 'AUD', 'createdByUserID': 13344081, 'alias': 'Primary', 'marginRate': '0.0333', 'lastTransactionID': '61', 'balance': '1014.3409', 'openTradeCount': 0, 'openPositionCount': 0, 'pendingOrderCount': 1, 'pl': '14.3528', 'resettablePL': '14.3528', 'resettablePLTime': '0', 'financing': '-0.0119', 'commission': '0.0000', 'dividendAdjustment': '0', 'guaranteedExecutionFees': '0.0000', 'unrealizedPL': '0.0000', 'NAV': '1014.3409', 'marginUsed': '0.0000', 'marginAvailable': '1014.3409', 'positionValue': '0.0000', 'marginCloseoutUnrealizedPL': '0.0000', 'marginCloseoutNAV': '1014.3409', 'marginCloseoutMarginUsed': '0.0000', 'marginCloseoutPositionValue': '0.0000', 'marginCloseoutPercent': '0.00000', 'withdrawalLimit': '1014.3409', 'marginCallMarginUsed': '0.0000', 'marginCallPercent': '0.00000'}, 'lastTransactionID': '61'}
# d_account = d_AccountSummary.get('account')

# x = float(d_account['resettablePL']) / float(d_account['balance']) * 100
# print(d_account)
# print('Result:')
# print(x)


import pytz, datetime
from datetime import timedelta

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
    
    
d = datetime.datetime.now() + timedelta(hours=-10)
e = d.strftime('%Y-%m-%dT%H:%M:%S.000000000Z')
print(e)

print('utc = ', strToTime(e, 'utc'))
print('no-utc = ', strToTime(e, None))
