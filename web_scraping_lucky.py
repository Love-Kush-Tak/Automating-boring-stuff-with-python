'''import requests, sys, webbrowser, bs4, html5lib
print('Googling...') # display text while downloading the Google page
search_term = 'python'
res = requests.get('http://google.com/search?q={0}'.format(search_term), 'lxml')
res.raise_for_status()
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'lxml')
# Open a browser tab for each result.
linkElems = soup.select('.r a')
print(len(linkElems))
#If you look up a little from the <a> element, though, there is an element like this: <h3 class="r">. r class is used only for search result links.
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    print(linkElems[i])'''
'''import requests
import sys
import webbrowser


word_to_search='test'

request = requests.get('http://google.com/search?q='+word_to_search)
content=request.content.decode('UTF-8','replace')

#
# Parse the content and get the links.  I had a problem with 
# bs4 so I manually searched over the content
#
links=[]
while '<h3 class="r">' in content:
    content=content.split('<h3 class="r">', 1)[1]
    split_content=content.split('</h3>', 1)
    link='http'+split_content[1].split(':http',1)[1].split('%',1)[0]
    links.append(link)
    content=split_content[1]


for link in links[:5]:  # max number of links 5
    webbrowser.open(link)'''
import requests, sys, webbrowser, bs4

search_term = 'python'

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q={0}'.format(search_term), 'lxml')
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Open a browser tab for each result.
linkElems = soup.select('.r')
print(linkElems)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

