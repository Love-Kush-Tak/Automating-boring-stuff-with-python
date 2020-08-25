import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, features="html.parser")
print(type(noStarchSoup))
#If a parser is not used then the following will occue
'''GuessedAtParserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.'''
exampleFile = open('example11.html')
#exampleSoup = bs4.BeautifulSoup(exampleFile, features = "html.parser")
#print(type(exampleSoup))
#exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features = "html.parser")
elems = exampleSoup.select('#author')
print(type(elems), elems)
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)


pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())

#The get() method for Tag objects makes it simple to access attribute values from an element
spanElem = exampleSoup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)










