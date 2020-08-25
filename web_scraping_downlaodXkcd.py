#downloadSkcd.py - Downloads every single XKCD comic
import requests, os, bs4
url = 'http://xkcd.com' # starting url
os.makedirs('xkcd', exist_ok=True) # store comics in./xkcd
while not url.endswith('#'):
    #TODO: Download the page
    print('Downloading page %s...' %url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features="lxml")
    #TODO: Find the url of the comic image
    #Find the url of the comic image
    comicElem = soup.select('#comic img') # the element with an id attribute comic and elemts under it named img
    if comicElem == []:
        print('Could not find comic image')
    else:
        comicUrl = comicElem[0].get('src').strip("http://")
        comicUrl="http://"+comicUrl
        if 'xkcd' not in comicUrl:
            comicUrl=comicUrl[:7]+'xkcd.com/'+comicUrl[7:]
        # Download the image
        print('Downloading image %s...' %(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    #TODO: Download the image-- done above
    #TODO: Save the image to./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    #TODO: Get the Prev btton's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done')
'''First, print url so that the user knows which URL the program is about to
download; then use the requests module’s request.get() function to download
it. As always, you immediately call the Response object’s raise_for_status()
method to throw an exception and end the program if something went
wrong with the download'''
