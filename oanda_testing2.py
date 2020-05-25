from oanda_class import kucingJoget, kucingTukang


y = kucingTukang()

print(y.strToTime('2020-05-21T22:35:00.000000000Z', None))
print(y.strToTime('2020-05-21T22:35:00.000000000Z', 'utc'))
print(y.strToTime('2020-05-21T22:35:00.000000000Z', 'local'))