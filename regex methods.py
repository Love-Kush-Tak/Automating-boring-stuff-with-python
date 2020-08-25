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


#Optional matching with the question mark
'''Sometimes there is a pattern that you want to match only optionally. That
is, the regex should find a match whether or not that bit of text is there.
The ? character flags the group that precedes it as an optional part of the
pattern'''
batRegex = re.compile(r'Bat(wo)?(man)')
mo = batRegex.search('Batman is an evil')
print(mo.group())
mo = batRegex.search('Batwoman is a devil')
print(mo.group())

mobile = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
findnum = mobile.search('My mobile number is 987-654-3210')
print(findnum.group())
findnum = mobile.search('My mobile number is 654-9871')
print(findnum.group())

#Matching zero or more with the star
'''The * (called the star or asterisk) means “match zero or more”—the group
that precedes the star can occur any number of times in the text. It can be
completely absent or repeated over and over again.'''
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('Batwowowowoman is woooo')
print(mo.group())
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('Batwoman is woooo')
print(mo.group())

#matching one or more with plus
'''While * means “match zero or more,” the + (or plus) means “match one or
more.” Unlike the star, which does not require its group to appear in the
matched string, the group preceding a plus must appear at least once.'''
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('Adventures of Batwowoman')
print(mo.group())
mo = batRegex.search('Adventrue of Batman')
if mo == None:
    print("true")
#matching specific repetitions with curly brackets
'''If you have a group that you want to repeat a specific number of times, follow
the group in your regex with a number in curly brackets. For example,
the regex (Ha){3} will match the string 'HaHaHa', but it will not match 'HaHa',
since the latter has only two repeats of the (Ha) group.
Instead of one number, you can specify a range by writing a minimum,
a comma, and a maximum in between the curly brackets. For example, the
regex (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.
You can also leave out the first or second number in the curly brackets
to leave the minimum or maximum unbounded. For example, (Ha){3,} will
match three or more instances of the (Ha) group, while (Ha){,5} will match
zero to five instances. Curly brackets can help make your regular expressions
shorter.'''
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('HaHaHa I am alive')
print(mo.group())
haRegex = re.compile(r'(Ha){3,}')
mo = haRegex.search('HaHaHaHaHaHa HiHiHiHi')
print(mo.group())
haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('Let me laugh 4 times at you HaHaHaHa')
print(mo.group())

# findall() method
'''In addition to the search() method, Regex objects also have a findall()
method. While search() will return a Match object of the first matched text
in the searched string, the findall() method will return the strings of every
match in the searched string.'''
PhoneNum = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = PhoneNum.findall('My new phone number is 900-495-8912 not 964-913-1406')
print(mo)

#character classes
'''\d Any numeric digit from 0 to 9.
\D Any character that is not a numeric digit from 0 to 9.
\w Any letter, numeric digit, or the underscore character.
(Think of this as matching “word” characters.)
\W Any character that is not a letter, numeric digit, or the
underscore character.
\s Any space, tab, or newline character. (Think of this as
matching “space” characters.)
\S Any character that is not a space, tab, or newline.'''

xmas = re.compile(r'\d+\s\w+')
match = xmas.findall('12 drummers, 3 hens, 2 doves, 5 peacocks, 845745 zebra, 8422ssd')
print(match)

#making own character classes using brackets []
vowel = re.compile(r'[aeiouAEIOU]')
print(vowel.findall('Robocop eats baby food. YA ITS TRUE'))
'''You can also include ranges of letters or numbers by using a hyphen.
For example, the character class [a-zA-Z0-9] will match all lowercase letters,
uppercase letters, and numbers.'''
''''Note that inside the square brackets, the normal regular expression
symbols are not interpreted as such. This means you do not need to escape
the ., *, ?, or () characters with a preceding backslash. For example, the
character class [0-5.] will match digits 0 to 5 and a period. You do not need
to write it as [0-5\.].
By placing a caret character (^) just after the character class’s opening
bracket, you can make a negative character class. A negative character class
will match all the characters that are not in the'''
consonant = re.compile(r'[^aeiouAEIOU]')
print(consonant.findall('Robo hero is a JACKPOT'))
'''You can also use the caret symbol (^) at the start of a regex to indicate that
a match must occur at the beginning of the searched text. Likewise, you can
put a dollar sign ($) at the end of the regex to indicate the string must end
with this regex pattern. And you can use the ^ and $ together to indicate
that the entire string must match the regex—that is, it’s not enough for a
match to be made on some subset of the string.'''
begins = re.compile(r'^Hello')
print(begins.findall('Hello world'))
print(begins.findall('World hello'))
ends = re.compile(r'Hello$')
print(ends.findall('Hello world'))
print(ends.findall('world Hello'))


#ends with a number
num_end = re.compile(r'\d$')
print(num_end.findall('Your number is 42'))
'''The r'^\d+$' regular expression string matches strings that both begin
and end with one or more numeric characters'''

whole = re.compile(r'^\d+')
print(whole.search('1234azsyd388'))
print(whole.search('1234 388').group())
whole = re.compile(r'\d+$')
print(whole.search('1234azsyd388').group())
print(whole.search('1234 388').group())
whole = re.compile(r'^\d+$')
print(whole.search('1234388').group())
print(whole.search('1234hgfd388'))
'''The . (or dot) character in a regular expression is called a wildcard and will
match any character except for a newline. For example, enter the following
into the interactive shell:'''
'''Remember that the dot character will match just one character, which
is why the match for the text flat in the previous example matched only lat.
To match an actual dot, escape the dot with a backslash: \..'''
at = re.compile(r'.at')
print(at.findall('cat, dog, rat, sat, mat, bat, fat, late, chapate'))

#macthing everything with dot star
'''Sometimes you will want to match everything and anything. For example,
say you want to match the string 'First Name:', followed by any and all text,
followed by 'Last Name:', and then followed by anything again. You can
use the dot-star (.*) to stand in for that “anything.” Remember that the
dot character means “any single character except the newline,” and the
star character means “zero or more of the preceding character.”'''
name1 = re.compile(r'First Name: (.*) Last Name: (.*)')
name = name1.search('First Name: Love Kush Last Name: Tak')
print(name.group(1), name.group(2))

'''The dot-star uses greedy mode: It will always try to match as much text as
possible. To match any and all text in a nongreedy fashion, use the dot, star,
and question mark (.*?). Like with curly brackets, the question mark tells
Python to match in a nongreedy way.'''

nogreedy = re.compile(r'<.*?>')
print(nogreedy.search('<To serve man> better>').group())
greedy = re.compile(r'<.*>')
print(greedy.search('<To serve man> better>').group())

#matching newlines with dot character
'''The dot-star will match everything except a newline. By passing re.DOTALL as
the second argument to re.compile(), you can make the dot character match
all characters, including the newline character.'''
nonewline = re.compile('.*')
print(nonewline.findall('Serve the nation \n Protect the country \n Love the nation'))
newline = re.compile('.*', re.DOTALL)
print(newline.findall('Serve the nation \n Protect the country \n Love the nation'))

#case-sensitive matching
'''Normally, regular expressions match text with the exact casing you specify.But sometimes you care only about matching the letters without worrying
whether they’re uppercase or lowercase. To make your regex case-insensitive,
you can pass re.IGNORECASE or re.I as a second argument to re.compile().'''
robocop = re.compile(r'tobocop', re.I)
print(robocop.findall('Tobocop is a TOBOcop, TOBOCOP is toBoCoP'))

#Substituting Strings with the sub() Method
'''Regular expressions can not only find text patterns but can also substitute
new text in place of those patterns. The sub() method for Regex objects is
passed two arguments. The first argument is a string to replace any matches.
The second is the string for the regular expression. The sub() method returns
a string with the substitutions applied.'''
names = re.compile(r'Agent \w+')
print(names.sub('Censored', ' Agent Alice gave the secret docs'))
'''Sometimes you may need to use the matched text itself as part of the
substitution. In the first argument to sub(), you can type \1, \2, \3, and so
on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.”
For example, say you want to censor the names of the secret agents by
showing just the first letters of their names. To do this, you could use the
regex Agent (\w)\w* and pass r'\1****' as the first argument to sub(). The \1
in that string will be replaced by whatever text was matched by group 1—
that is, the (\w) group of the regular expression.'''
agent = re.compile(r'Agent (\w)\w*')
print(agent.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
agent = re.compile(r'Agent \w*')
print(agent.sub('yese', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

      




















































