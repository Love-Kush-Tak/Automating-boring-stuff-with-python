import os
print(os.path.join('F','Highways_intern','highway_slides'))
myFiles = ['account.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('F:\Highways_intern\highway_slides', filename))

#current working directory
    '''>>> import os
>>> os.getcwd()
'C:\\Python34'
>>> os.chdir('C:\\Windows\\System32')
>>> os.getcwd()
'C:\\Windows\\System32'''
# creating new folders using os.makedirs()

# os.makedirs('F:\delicious\wallnut\waffles')

#Handling abosulte and relative paths
print(os.path.abspath('.'))
print(os.path.abspath('.\\Scripts'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))
'''Calling os.path.relpath(path, start) will return a string of a relative path
from the start path to path. If start is not provided, the current working
directory is used as the start path.'''

print(os.path.relpath('C:\\Users\\pc\\python', 'C:\\'))
'''Calling os.path.dirname(path) will return a string of everything that comes
before the last slash in the path argument. Calling os.path.basename(path) will
return a string of everything that comes after the last slash in the path argument.'''
path = 'C:\\Users\\pc\\python'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))
print(path.split(os.path.sep))
print(os.path.getsize('C:\\Users\\pc\\python'))
totalSize = 0
for filename in os.listdir('C:\\Users\\pc\\python'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\pc\\python', filename))
print(totalSize)
'''Calling os.path.exists(path) will return True if the file or folder referred
to in the argument exists and will return False if it does not exist.
• Calling os.path.isfile(path) will return True if the path argument exists
and is a file and will return False otherwise.
• Calling os.path.isdir(path) will return True if the path argument exists
and is a folder and will return False otherwise.'''
            
print(os.path.exists('C:\\Users\\pc\\python'))
print(os.path.exists('adj:'))
print(os.path.isfile('C:\\Users\\pc\\python'))
print(os.path.isdir('C:\\Users\\pc\\python'))
print(os.path.isfile('C:\\Users\\pc\\python\\Python36-32\\add.py'))
'''For instance, if I wanted to check for a flash drive with the volume
named D:\ on my Windows computer'''
print(os.path.exists('D:\\'))
'''To open a file with the open() function, you pass it a string path indicating
the file you want to open; it can be either an absolute or relative path. The
open() function returns a File object.'''
openfile = open('C:\\Users\\Public\\hello.docx', 'r',  encoding='utf8', errors='ignore')
opencontent = openfile.read()
sonnetfile = open('C:\\Users\\pc\\sonnet29.docx', 'r', encoding='ISO-8859-1')
sonnetfile.readlines()
sonnetfile2 = open('C:\\Users\\pc\\sonnet30.txt')
sonnetfile2.readlines()

#Write and append mode

'''Write mode will overwrite the existing file and start from scratch, just
like when you overwrite a variable’s value with a new value. Pass 'w' as the
second argument to open() to open the file in write mode. Append mode,
on the other hand, will append text to the end of the existing file. You can
think of this as appending to a list in a variable, rather than overwriting the
variable altogether. Pass 'a' as the second argument to open() to open the
file in append mode.'''
'''If the filename passed to open() does not exist, both write and append
mode will create a new, blank file. After reading or writing a file, call the
close() method before opening the file again.'''

baconfile = open('bacon.txt', 'w')
baconfile.write('Hello World!\n')
baconfile.close()
baconfile = open('bacon.txt', 'a')
baconfile.write('Bacon is not a vegetable')
baconfile.close()
baconfile = open('bacon.txt')
content = baconfile.read()
baconfile.close()
print(content)

#saving variables with the shelve module

import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
'''After running the previous code on Windows, you will see three new files
in the current working directory: mydata.bak, mydata.dat, and mydata.dir.'''
shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

import pprint
cats = [{'name': 'Zophie', 'desc' :'chubby'}, {'name': 'pooka', 'desc' :'fluffy'}]
print(pprint.pformat(cats))
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) +'\n')
fileObj.close()
'''Here, we import pprint to let us use pprint.pformat(). We have a list of
dictionaries, stored in a variable cats. To keep the list in cats available even
after we close the shell, we use pprint.pformat() to return it as a string. Once
we have the data in cats as a string, it’s easy to write the string to a file, which
we’ll call myCats.py.
The modules that an import statement imports are themselves just
Python scripts. When the string from pprint.pformat() is saved to a .py file,
the file is a module that can be imported just like any other.'''

import myCats
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])

                                               
      





