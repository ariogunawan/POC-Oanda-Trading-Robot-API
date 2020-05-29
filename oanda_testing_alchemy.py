import pandas as pd
import pymysql
from sqlalchemy import create_engine

cnx = create_engine('mysql+pymysql://root:kucingjoget@localhost/oanda')    
df = pd.read_sql('SELECT error_log_id, error_log_message FROM error_log', cnx) #read the entire table
res = df.to_dict()
error_log_id = res['error_log_id']
error_log_message = res['error_log_message']

for x in error_log_id:
    s = 'update error_log set error_log_message = ''' + str(error_log_id[x]) + ' where error_log_id = ''' + str(error_log_message[x]) + ''
    print(s)