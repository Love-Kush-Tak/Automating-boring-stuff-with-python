import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
'''when Python logs an event, it creates a LogRecord object that holds information
about that event. The logging module’s basicConfig() function lets you
specify what details about the LogRecord object you want to see and how you
want those details displayed'''
#you can always disable logging module later by adding a single logging.disable(logging.CRITICAL)
logging.debug('Start  of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' %(n))
    total = 1
    for i in range(n+1):
        total *= i
        logging.debug('i is ' + str(i) +', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' %(n))
    return total

print(factorial(5))
logging.debug('End of program')

def factorial1(n):
    logging.debug('Start of factorial(%s%%)' %(n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is ' + str(i) +', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' %(n))
    return total

print(factorial1(5))
logging.debug('End of program')

logging.debug('Some debug details.')
logging.info('The loggging module is working')
logging.warning('An error message is about to be logged')
logging.error('An error has ocurred.')
logging.critical('The program is unable to recover!')
'''But after developing your program
some more, you may be interested only in errors. In that case, you can set
basicConfig()’s level argument to logging.ERROR. This will show only ERROR
and CRITICAL messages and skip the DEBUG, INFO, and WARNING
messages.'''
'''if you want to disable
logging entirely, just add logging.disable(logging.CRITICAL) to your program.'''
logging.critical('Critical error! Critical error!')
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')

#Logging to a file














