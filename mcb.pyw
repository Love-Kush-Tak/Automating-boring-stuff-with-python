#mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
'''Copying and pasting will require the pyperclip module, and reading
the command line arguments will require the sys module. The shelve module
will also come in handy: Whenever the user wants to save a new piece
of clipboard text, you’ll save it to a shelf file. Then, when the user wants to
paste the text back to their clipboard, you’ll open the shelf file and load it
back into your program. The shelf file will be named with the prefix mcb'''
#Save Clipboard content with a keyword
if  len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #TODO: List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    
mcbShelf.close()





'''If the first command line argument (which will always be at index 1
of the sys.argv list) is 'save' u, the second command line argument is the
keyword for the current content of the clipboard. The keyword will be used
as the key for mcbShelf, and the value will be the text currently on the clipboard'''
