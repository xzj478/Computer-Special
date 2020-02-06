Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======================== RESTART: /home/user/test.py ========================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/test.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/test.py', 'a': 10, 'b': 1.1, 'c': 'd'}
>>> mike76 = 'big parade'
>>> 76mike = 6
SyntaxError: invalid syntax
>>> more of = 4
SyntaxError: invalid syntax
>>> more jjj = 5
SyntaxError: invalid syntax
>>> ty_76 = 6
>>> minute = 59
>>> minute/60
0.9833333333333333
>>> minute//60
0
>>> x = 5
>>> x+1
6
>>> (2)*(2*5)**(3)
2000
>>> quotient = 7//3
>>> 7//3
2
>>> 7%3
1
>>> first = '100'
>>> second = '150
SyntaxError: EOL while scanning string literal
>>> second = '150'
>>> first + second
'100150'
>>> type(first)
<class 'str'>
>>> a = "Test "
>>> second = 5
>>> first * second
'100100100100100'
>>> a * second
'Test Test Test Test Test '
>>> c = '3'
>>> a * c
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a * c
TypeError: can't multiply sequence by non-int of type 'str'
>>> inp = input
>>> inp
<built-in function input>
>>> inp = input()
Hello world
>>> inp
'Hello world'
>>> name = input('What is your name?\n')
What is your name?
Zijian
>>> name
'Zijian'
>>> str(name)
'Zijian'
>>> int(name)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(name)
ValueError: invalid literal for int() with base 10: 'Zijian'
>>> age = input('How old are you?\n')
How old are you?
59
>>> age
'59'
>>> int(age)
59
>>> # That'š the comment
>>> for word in words:
	print(word)

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    for word in words:
NameError: name 'words' is not defined
>>> words = ['d', 'mike', 'Jack']
>>> word
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    word
NameError: name 'word' is not defined
>>> for word in words:
	print(word)

d
mike
Jack
>>> e = 03
SyntaxError: invalid token
>>> pi
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
>>> float(pi)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    float(pi)
NameError: name 'pi' is not defined
>>> name = input('Enter your name:\n');
Enter your name:
Zijian
>>> print('Hello' name)
SyntaxError: invalid syntax
>>> print('Hello')
Hello
>>> Enter Hours: 35
SyntaxError: invalid syntax
>>> Hours = input()
35
>>> Rate = input()
2.75
>>> Pay = Hours * Rate
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    Pay = Hours * Rate
TypeError: can't multiply sequence by non-int of type 'str'
>>> Pay = Hours*Rate
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    Pay = Hours*Rate
TypeError: can't multiply sequence by non-int of type 'str'
>>> Hours * Rate
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    Hours * Rate
TypeError: can't multiply sequence by non-int of type 'str'
>>> Rate
'2.75'
>>> a = 5
>>> a
5
>>> int(Hours)
35
>>> int(Rate)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    int(Rate)
ValueError: invalid literal for int() with base 10: '2.75'
>>> float(Rate)
2.75
>>> Pay = Hours * Rate
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    Pay = Hours * Rate
TypeError: can't multiply sequence by non-int of type 'str'
>>> Hours
'35'
>>> Pay = int(Hours) * float(Rate)
>>> Pay
96.25
>>> Hello world
SyntaxError: invalid syntax
>>> print('Hello name')
Hello name
>>> print('Hello' str(name))
SyntaxError: invalid syntax
>>> print(name)
Zijian
>>> print('Hello',name)
Hello Zijian
>>> width = 17
>>> height = 12.0
>>> width//2
8
>>> width/2.0
8.5
>>> height/3
4.0
>>> width/2
8.5
>>> 1+2*5
11
>>> raw_input
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    raw_input
NameError: name 'raw_input' is not defined
>>> type(Hours)
<class 'str'>
>>> int a = input('Enter number:\n')
SyntaxError: invalid syntax
>>> 
======================== RESTART: /home/user/test.py ========================
Enter your name:
Zijian
Hello Zijian
Enter Hours:
35
Enter Rate:
2.75
Pay:  96.25
>>> 
