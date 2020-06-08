
import pytz, datetime
from datetime import timedelta

def strToTime(time, utc):
    local_timezone = pytz.timezone('Australia/Sydney')
    oanda_time_format = '%Y-%m-%dT%H:%M:%S.000000000Z'
    mysql_time_format = '%Y-%m-%d %H:%M:%S'
    # change raw string datetime to datetime object
    raw_datetime = datetime.datetime.strptime(time, oanda_time_format)
    utc_timezone = pytz.utc
    # set the raw datetime as UTC timezone
    utc_datetime = utc_timezone.localize(raw_datetime)
    # set local datetime based on utc_datetime by changing its timezone
    local_datetime = utc_datetime.astimezone(local_timezone)
    # format both as mysql datetime format
    utctime = utc_datetime.strftime(mysql_time_format)
    localtime = local_datetime.strftime(mysql_time_format)
    return utctime if not(utc is None) and utc.upper() == 'UTC' else localtime 
    
oanda_timeformat = '%Y-%m-%dT%H:%M:%S.000000000Z'    
d = datetime.datetime.now() + timedelta(hours=-10)
str_oandatime = d.strftime(oanda_timeformat)

print('UTC time : ', strToTime(str_oandatime, 'utc'))
print('Local time : ', strToTime(str_oandatime, None))
