import datetime
#converting datetime objects into strings
oct21st = datetime.datetime(2015,10,31,16,29,0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))
#converting strings into datetime objects
print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
print(datetime.datetime.strptime('2105/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime("October of '15", "%B of '%y"))
