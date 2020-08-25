# matching multiple groups with the pipe (|)
import re
hero = re.compile(r'Batman|Tina Fey')
'''When both Batman and Tina Fey occur in the searched string, the first
occurrence of matching text will be returned as the Match object'''
mo1 = hero.search('Batman and Tina Fey')
print(mo1.group())
mo2 = hero.search('Tina Fey is a super')
print(mo2.group())
'''For example, say you wanted to match any of the strings 'Batman',
'Batmobile', 'Batcopter', and 'Batbat'. Since all these strings start with Bat, it
would be nice if you could specify that prefix only once. This can be done
with parentheses.'''
batRegex = re.compile(r'Bat(man|mobile|girl|copter)')
mo = batRegex.search('Batgirl is a lady bat')
print(mo.group())
print(mo.group(1))
'''If you need to match an actual pipe character, escape it with a backslash,
like \|.'''
