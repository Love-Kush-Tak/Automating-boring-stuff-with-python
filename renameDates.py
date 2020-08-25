#create a regex for American-style dates
import shutil, os,re
'''re.VERBOSE : This flag allows you to write regular expressions that look nicer and are more readable by allowing you to visually separate logical sections of the pattern and add comments.
Whitespace within the pattern is ignored, except when in a character class, or when preceded by an unescaped backslash, or within tokens like *?, (?: or (?P. When a line contains a # that is not in a character class and is not preceded by an unescaped backslash, all characters from the leftmost such # through the end of the line are ignored.'''
datePattern = re.compile(r"""^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""", re.VERBOSE)
'''all text before the date, one or two digits for the month, one or two digits for the day,four digits for the year, all text after the date)'''
os.chdir('F:/')
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    #skip files without a date
    if mo == None:
        continue

    #Get the differnet parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    #Form the European-style filename
    euroFilename = beforePart + dayPart +'-'+ monthPart + '-' + yearPart + afterPart

    #Get the full, absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    #Rename the files
    print('Renaming "%s" to "%s" ...'%(amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename) # uncomment after testing







    
    


