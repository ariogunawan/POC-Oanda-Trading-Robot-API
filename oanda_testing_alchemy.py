from sqlalchemy import create_engine
import pandas as pd
from talib.abstract import SMA

cnx = create_engine('mysql+pymysql://root:kucingjoget@localhost/oanda')
df = pd.read_sql('SELECT price_id, open, high, low, close from price where price_id >= 1408', cnx) #read the entire table

#x['slowk'], x['slowd'] = STOCH(inputs, 5, 1, 0, 3, 0, prices=['high', 'low', 'close'])
df['sma_5'] = SMA(df, timeperiod=5, price='open')
#print(df)

df.to_sql(name='oandatemptable', con=cnx, if_exists='replace')
sql = "update indicator i " \
      "join oandatemptable t on t.price_id = i.price_id_fk " \
      "SET i.sma_5 = ROUND(t.sma_5, 8)" \
      "where t.sma_5 is not null "

cnx.execute(sql)
cnx.dispose()
