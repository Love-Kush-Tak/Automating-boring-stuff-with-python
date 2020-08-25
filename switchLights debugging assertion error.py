'''Say you’re building a traffic light simulation program. The data structure
representing the stoplights at an intersection is a dictionary with
220 Chapter 10
keys 'ns' and 'ew', for the stoplights facing north-south and east-west,
respectively. The values at these keys will be one of the strings 'green',
'yellow',
or 'red'.'''
# finding bugs in Traffic lights switching
market_2nd = {'ns':'green', 'ew':'red'}
mission_16th = {'ns':'red', 'ew':'green'}
'''These two variables will be for the intersections of Market Street and
2nd Street, and Mission Street and 16th Street'''
def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] =='green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] =='red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
switchLights(market_2nd)
