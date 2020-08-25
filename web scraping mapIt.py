import webbrowser, sys
#webbrowser.open('http://inventwithpython.com/')
#webbrowser.open('http://maps.google.com/')
if len(sys.argv) > 1:
    #Get address from command line.
    address = ''.join(sys.argv[1:])

