'''query : query string that we want to search for.
tld : tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
lang : lang stands for language.
num : Number of results we want.
start : First result to retrieve.
stop : Last result to retrieve. Use None to keep searching forever.
pause : Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
Return : Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.'''

import googlesearch, bs4, webbrowser, sys
try:
    from googlesearch import search
except ImportError:
    print("NJo module named 'google' found")

# to search
query = input()

for j in search(query, tld="com", num=10,stop =10, pause=2):
    print(j)
    webbrowser.open(j)
