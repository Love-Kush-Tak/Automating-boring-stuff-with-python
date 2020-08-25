'''Raising an exception is a way of saying, “Stop running the code in this function
and move the program execution to the except statement.”'''
import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt' ,'w')
    errorFile.write(traceback.format_exc())'''This function is useful if you want the information from an exception’s traceback but also want an except statement to gracefully handle the exception'''
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')
