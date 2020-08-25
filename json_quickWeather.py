import json, requests, sys
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ''.join(sys.argv[1:])
#Download the JSON data from OPenWeather.org's API
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3'%(location)
response = requests.get(url)
response.raise_for_status()
#TODO: Load JSON data into a Python variable
weatherData = json.loads(response.text)
#Print weather descriptions
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[o]['weather'][0]['description'])
print()
print('Tomorrow')
print(w[1]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Day after tomorrow')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])






