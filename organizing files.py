import shutil, os
'''The shutil (or shell utilities) module has functions to let you copy, move,
rename, and delete files in your Python programs'''
#shutil.copy(source, destination)
os.chdir('F:\\')
#shutil.copy('F:/automate-the-boring-stuff-with-python-2015-.pdf', 'F:/Highways_intern')
'''While shutil.copy() will copy a single file, shutil.copytree() will
copy an entire folder and every folder and file contained in it.'''
#shutil.copytree( source, destination)
#shutil.copytree('F:/robotic process automation', 'F:/robotics process automation_backup')
#Moving and renaming files and folders: shutil.move(source, destination)
#shutil.move('F:/Predictive Analysis', 'F:/Highways_intern')
#shutil.move('F:/Highways_intern/Predictive Analysis' , 'F:')

#Permanently deleting files and folders

#os.unlink(path) will delete the file at path
#os.rmdir(path) will delete thr folder at path. This folder must be empty of any files or folders
#shutil.rmtree(path) will remove the folder at path
'''a Python program that was intended to delete files that have the .txt file
extension but has a typo (highlighted in bold) that causes it to delete .rxt
files instead:'''
'''import os
for filename in os.listdir():
if filename.endswith('.rxt'):
os.unlink(filename)'''
'''If you had any important files ending with .rxt, they would have been
accidentally, permanently deleted. Instead, you should have first run the
program like this'''
'''import os
for filename in os.listdir():
if filename.endswith('.rxt'):
#os.unlink(filename)
print(filename)'''
#Using send2trash is much safer than Python’s regular delete functions, because it will send folders and files to your computer’s trash or recycle bin instead of permanently deleting them.

import send2trash
baconFile = open('bacon1.txt' , 'a') #creates the file
baconFile.write('Bacon is not a vegetable')
baconFile.close()
send2trash.send2trash('bacon1.txt')
'''Note that the send2trash()
function can only send files to the recycle bin; it cannot pull files out of it.'''

#os.makedirs('F:\\delicious\\cats\\catnames.txt')
#os.makedirs('F:\\delicious\\cats\\zophie.jpg')
#os.makedirs('F:\\delicious\\walnut\\waffles\\butter.txt')
#os.makedirs('F:\\delicious\\spam.txt')

for folderName, subfolders, filenames in os.walk('F:\\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ':' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ':' +filename)

    print('')

'''The os.walk() function is passed a single string value: the path of a
folder. You can use os.walk() in a for loop statement to walk a directory
tree, much like how you can use the range() function to walk over a range of
numbers. Unlike range(), the os.walk() function will return three values on
each iteration through the loop:
1. A string of the current folder’s name
2. A list of strings of the folders in the current folder
3. A list of strings of the files in the current folder'''

import zipfile, os
os.chdir('C:/Users/pc/Downloads')
Zip = zipfile.ZipFile('Deflection angle & Length of curve calculation.zip')
#Zip.namelist()
spamInfo = Zip.getinfo('Lecture 30 -Concluding Session and Revisions.pdf')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size/spamInfo.compress_size, 2)))
#Zip.close()

# Extracting from ZIP files
'''The extractall() method for ZipFile objects extracts all the files and folders
from a ZIP file into the current working directory.'''
Zip.extractall()
#Zip.close()
'''After running this code, the contents of example.zip will be extracted
to C:\. Optionally, you can pass a folder name to extractall() to have it
extract the files into a folder other than the current working directory. If
the folder passed to the extractall() method does not exist, it will be created.
For instance, if you replaced the call at u with exampleZip.extractall('C:\\
delicious'), the code would extract the files from example.zip into a newly
created C:\delicious folder.'''
'''The extract() method for ZipFile objects will extract a single file from
the ZIP file. Continue the interactive shell example:'''
Zip.extract('Transition curve length calculation & Set back distance_Anuj.xls', 'F:\\Highways_intern')
Zip.close()
os.chdir('F:/Highways_intern')
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('2.-ReCAP-HVT-Project-Concept-Note-Template-FINAL.docx' , compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
'''When you pass a path to the write() method of a ZipFile object, Python
will compress the file at that path and add it into the ZIP file. The write()
method’s first argument is a string of the filename to add. The second argument
is the compression type parameter, which tells the computer what algorithm
it should use to compress the files; you can always just set this value to
zipfile.ZIP_DEFLATED'''




