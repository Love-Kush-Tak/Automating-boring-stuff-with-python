def isPhoneNumber(text):
    if len(text)!= 12:
        return False
    for i in range(3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
       if not text[i].isdecimal():
           return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    if isPhoneNumber(message[i:i+12]):
        print("Phone number found", message[i:i+12])

#Using regex methods
import re
phoneNumRegex = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 879-987-4521')
print('Phone number found: ', mo.group())

#removing area code from the phone number
phoneNumReg = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
match = phoneNumReg.search('My phone number is 879-654-3210')
print(match.group(1), match.group(), match.group(2), match.group(0))
# to retrieve all the groups 
print(match.groups())
areaCode, mainNumber = match.groups()
print(areaCode)
print(mainNumber)
               
                     
