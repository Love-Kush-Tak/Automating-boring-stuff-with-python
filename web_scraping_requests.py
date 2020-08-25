import requests
#Downloading a Web Page with the requests.get() Function
'''The requests.get()function takes a string of a URL to download. By calling
type() on requests.get()’s return value, you can see that it returns a Response
object, which contains the response that the web server gave for your request.'''
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))
if(res.status_code == requests.codes.ok):
    print("True")
'''You can tell that the request for this web
page succeeded by checking the status_code attribute of the Response object. If it is equal to the value of requests.codes.ok, then everything went fine. (Incidentally, the status code for “OK” in the HTTP protocol is 200. You
may already be familiar with the 404 status code for “Not Found.”)'''
'''the Response object has a status_code attribute that can be
checked against requests.codes.ok to see whether the download succeeded'''
print(len(res.text))
print(res.text[:250])

#Checking for errors
'''A
simpler way to check for success is to call the raise_for_status() method on
the Response object. This will raise an exception if there was an error downloading
the file and will do nothing if the download succeeded'''
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
#res.raise_for_status()
'''If a failed download isn’t
a deal breaker for your program, you can wrap the raise_for_status() line
with try and except statements to handle this error case without crashing'''
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))



