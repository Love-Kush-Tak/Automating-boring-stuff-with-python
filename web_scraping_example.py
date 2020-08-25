import requests
res = requests.get('http://nostarch.com/automatestuff/')
res.raise_for_status()
playFile = open('example.html','wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
