'''Assertion is a sanity check to make sure your code isn't doing something obviously worng. These checks are performed by assert statements. If the sanity check fails, then an AssertionError exception is raised'''
'''In code, an assert statement consists of the following:
1) the assert keyword
2) A condition (i.e., an expression that evaluates to True or False)
3) A comma
4) A string to display when the condiotion is False'''
podBayDoorStatus = 'open'
assert podBayDoorStatus ==  'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus =='open', 'The pod bay doors need to be "open".'
'''In plain English, an assert statement says, “I assert that this condition
holds true, and if not, there is a bug somewhere in the program.” Unlike
exceptions, your code should not handle assert statements with try and
except; if an assert fails, your program should crash. By failing fast like this,
you shorten the time between the original cause of the bug and when you
first notice the bug. This will reduce the amount of code you will have to
check before finding the code that’s causing the bug.'''
'''Assertions are for programmer errors, not user errors. For errors that
can be recovered from (such as a file not being found or the user entering
invalid data), raise an exception instead of detecting it with an assert
statement.'''



    
            
