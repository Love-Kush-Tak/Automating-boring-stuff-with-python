import requests, os, bs4, threading
os.chdir('F://')
os.makedirs('xkcd', exist_ok=True)
def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading page http://xkcd.com/%s...' %(urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        if res.status_code != 200:
            continue
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features="lxml")
        #Find the url of the comic image
        comicElem = soup.select('#comic img') # the element with an id attribute comic and elemts under it named img
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src').strip("http://")
            comicUrl = "http://" + comicUrl
            if 'xkcd' not in comicUrl:
                comicUrl=comicUrl[:7]+'xkcd.com/'+comicUrl[7:]
            #Download the image
            print('Downloading the image %s...' %(comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
            #Save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

#Create and start the Thread objects
downloadThreads = []  #list of all the Thread Objects
for i in range(1,501, 100):    #loop 14 times, create 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i,i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()
#Wait for all the threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done')
            
