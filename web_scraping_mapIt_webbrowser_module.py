import webbrowser, sys, pyperclip
#webbrowser.open('http://inventwithpython.com/')
#webbrowser.open('http://maps.google.com/')
if len(sys.argv) > 1:
    #Get address from command line.
    address = ''.join(sys.argv[1:])
else:
    #Get address from the clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
'''Command line arguments are usually separated by spaces, but in
this case, you want to interpret all of the arguments as a single string. Since
sys.argv is a list of strings, you can pass it to the join() method, which returns
a single string value. You don’t want the program name in this string, so
instead of sys.argv, you should pass sys.argv[1:] to chop off the first element
of the array. The final string that this expression evaluates to is stored in
the address variable.'''
    

