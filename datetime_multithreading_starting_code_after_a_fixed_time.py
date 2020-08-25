import time, datetime
startTime = datetime.datetime(2020,8,17,17, 53,0)
while datetime.datetime.now()<startTime:
    time.sleep(5)
print('Program now starting on Hallowen 2029')
import threading
print('Start of the program')
def takeANap():
    time.sleep(5)
    print('Wake up')
threadObj = threading.Thread(target=takeANap)
threadObj.start()
print('End of program')
'''This print() call has three regular arguments, 'Cats', 'Dogs', and 'Frogs',
and one keyword argument, sep=' & '. The regular arguments can be passed
Keeping Time, Scheduling Tasks, and Launching Programs 349
as a list to the args keyword argument in threading.Thread(). The keyword
argument can be specified as a dictionary to the kwargs keyword argument
in threading.Thread().'''
print('Cats', 'Dogs', 'Frogs' , sep=' & ')
threadObj = threading.Thread(target=print, args=['Cats','Dogs','Frogs'], kwargs={'sep':' & '})
'''What this ends up doing is calling the print() function and passing its
return value (print()’s return value is always None) as the target keyword
argument. It doesn’t pass the print() function itself. When passing arguments
to a function in a new thread, use the threading.Thread() function’s
args and kwargs keyword arguments.'''

threadObj.start()
