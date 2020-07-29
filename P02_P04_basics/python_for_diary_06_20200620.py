Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit = 'banana'
>>> fruit[1]
'a'
>>> fruit[1.5]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    fruit[1.5]
TypeError: string indices must be integers
>>> len(fruit)
6
>>> los = len(fruit)
>>> fruit[los]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    fruit[los]
IndexError: string index out of range
>>> fruit[los-1]
'a'
>>> index = 0
>>> while index<len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
b
a
n
a
n
a
>>> for char in fruit:
	print(char)

	
b
a
n
a
n
a
>>> s = 'Monty Python'
>>> s[0:5]
'Monty'
>>> s[6:12]
'Python'
>>> fruit[:3]
'ban'
>>> 
>>> fruit[3:]
'ana'
>>> greeting = 'Hello, World!'
>>> greeting[0]
'H'
>>> greeting[0] = 'J'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    greeting[0] = 'J'
TypeError: 'str' object does not support item assignment
>>> greeting[0] = J
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    greeting[0] = J
NameError: name 'J' is not defined
>>> greet = 'J'+ greeting[1:]
>>> greet
'Jello, World!'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count = count++
		
SyntaxError: invalid syntax
>>> for letter in fruit:
	if letter == 'a':
		count = count + 1

		
>>> count
3
>>> a in fruit
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a in fruit
NameError: name 'a' is not defined
>>> 'a' in fruit
True
>>> 'ban' in fruit
True
>>> 'and' in fruit
False
>>> if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

    
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    if word < 'banana':
NameError: name 'word' is not defined
>>> word = input()
apple
>>> if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

    
Your word,apple, comes before banana.
>>> dir(fruit)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> type(fruit)
<class 'str'>
>>> new_fruit = fruit.upper()
>>> new_fruit
'BANANA'
>>> fruit.find('ana')
1
>>> fruit.find('a',4)
5
>>> fruit.find('a',5)
5
>>> fruit.find('a',6)
-1
>>> fruit.find('a',7)
-1
>>> fruit.find('a',-1)
5
>>> fruit.find('a',-2)
5
>>> fruit.find('a',-3)
3
>>> line = ' Hello  World    I  Love YOU'
>>> line.strip()
'Hello  World    I  Love YOU'
>>> line.startwith('H')
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    line.startwith('H')
AttributeError: 'str' object has no attribute 'startwith'
>>> type(line)
<class 'str'>
>>> line.startswith('H')
False
>>> line.startswith(' ')
True
>>> line.startswith(' H')
True
>>> line.upper()
' HELLO  WORLD    I  LOVE YOU'
>>> line.lower()
' hello  world    i  love you'
>>> line.lower().startswith(' h')
True
>>> data = 'From xzjmichael@gmail.com 20/06/2020'
>>> at = data.find('@')
>>> space = data.find(' ',at)
>>> email_addrs = data[at:space-1]
>>> email_addrs
'@gmail.co'
>>> email_addrs = data[at+1:space]
>>> email_addrs
'gmail.com'
>>> fruit[3:5]
'an'
>>> camels = 42
>>> '%d' % camels
'42'
>>> 'I have spotted %d camels''
SyntaxError: EOL while scanning string literal
>>> 'I have spotted %d camels'
'I have spotted %d camels'
>>> 'I have spotted %d camels',% camels
SyntaxError: invalid syntax
>>> 'I have spotted %d camels',% camels
SyntaxError: invalid syntax
>>> 'I have spotted %d camels' % camels
'I have spotted 42 camels'
>>> 'In %d years I have spotted %g %s.'(3, 0.1, 'camels')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    'In %d years I have spotted %g %s.'(3, 0.1, 'camels')
TypeError: 'str' object is not callable
>>> 'In %d years I have spotted %g %s.'%(3, 0.1, 'camels')
'In 3 years I have spotted 0.1 camels.'
>>> '%d %d %d' % (1, 2)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    '%d %d %d' % (1, 2)
TypeError: not enough arguments for format string
>>> '%d %d %d' % (1, 2, 3)
'1 2 3'
>>> '%d %d %d' % (1, 2, 3)
'1 2 3'
>>> while True:
	line = input('> ')
	if line[0] == '#':
		continue
	if line == 'done':
		break
	print(line)

	
> #
> l
l
> j
j
> ###
> ji
ji
> done
>>> 
