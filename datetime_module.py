import datetime, time
print(datetime.datetime.now())
dt = datetime.datetime(2015,10, 21,16,29,0)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
print(datetime.datetime.fromtimestamp(1000000))
print(datetime.datetime.fromtimestamp(time.time()))
hallowen2015 = datetime.datetime(2015,10,31,0,0,0)
newyears2016 = datetime.datetime(2015,1,1,0,0,0)
oct31_2015 = datetime.datetime(2015,10,31,0,0,0)
print(hallowen2015 > newyears2016)
print(newyears2016 > hallowen2015)
print( newyears2016 != oct31_2015)
# timedelta - represents a duration of time rather than a moment in time
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)

#Arithmetic operators on data arithmetic
dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)

oct21st = datetime.datetime(2020, 10,20,21,16,12)
aboutThirtyYears = datetime.timedelta(days = 30*365)
print(oct21st - aboutThirtyYears)
print(oct21st +  aboutThirtyYears)
#Pausing until a Specific Date
#hallowen2020 = datetime.datetime(2020, 10, 31, 0,0,0)
'''while datetime.datetime.now() < hallowen2020:
    time.sleep(1)'''
