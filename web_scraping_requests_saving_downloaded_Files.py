'''you can save the web page to a file on your hard drive with the
standard open() function and write() method. There are some slight differences,
though. First, you must open the file in write binary mode by passing
the string 'wb' as the second argument to open().'''
import requests
res = requests.get('http://lists.iitb.ac.in/pipermail/student-notices/attachments/20200730/083a108e/attachment.pdf')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
'''The iter_content() method returns “chunks” of the content on each
iteration through the loop. Each chunk is of the bytes data type, and you
get to specify how many bytes each chunk will contain'''
'''<http://lists.iitb.ac.in/pipermail/student-notices/attachments/20200730/083a108e/attachment.pdf'''
'''http://www.gutenberg.org/cache/epub/1112/pg1112.txt'''
