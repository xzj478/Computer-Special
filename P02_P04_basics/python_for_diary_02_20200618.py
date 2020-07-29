Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(4)
4
>>> type('Hello, World!')
<class 'str'>
>>> type(17)
<class 'int'>
>>> type(3.2)
<class 'float'>
>>> type('17')
<class 'str'>
>>> type('3.2')
<class 'str'>
>>> print(1000000)
1000000
>>> print(1,000,000)
1 0 0
>>> message = 'And now for somthing completely different'
>>> n = 17
>>> pi
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
>>> pi = 3.14159265358
>>> print(pi)
3.14159265358
>>> print(n)
17
>>> print(message)
And now for somthing completely different
>>> type(message)
<class 'str'>
>>> 76sth = 'huge'
SyntaxError: invalid syntax
>>> class = 'thx'
SyntaxError: invalid syntax
>>> more@ = 5
SyntaxError: invalid syntax
>>> print(1)
1
>>> x = 2
>>> print(x);
2
>>> 20+32
52
>>> hour-1
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    hour-1
NameError: name 'hour' is not defined
>>> hour = 24
>>> hour = 60
>>> hour - 1
59
>>> 5**2
25
>>> 5**3
125
>>> 59/60
0.9833333333333333
>>> 59//60
0
>>> 7//3
2
>>> 7%3
1
>>> first = 10
>>> second = 15
>>> first+second
25
>>> a = '10'
>>> b = '15'
>>> a+b
'1015'
>>> a=3
>>> b='test'
>>> a+b
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a*b
'testtesttest'
>>> inp=input()
I love you
>>> inp
'I love you'
>>> print(inp)
I love you
>>> name=input('whats your name?#n')
whats your name?#n
>>> name=input('whats your name?\n')
whats your name?
michael
>>> name
'michael'
>>> print(name)
michael
>>> ques1='n'
>>> ques1
'n'
>>> print(ques1)
n
>>> q1=what
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    q1=what
NameError: name 'what' is not defined
>>> q1='whats your name?\n'
>>> name=input(q1)
whats your name?
michael
>>> name
'michael'
>>> int(name)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    int(name)
ValueError: invalid literal for int() with base 10: 'michael'
>>> str(name)
'michael'
>>> name+5
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    name+5
TypeError: can only concatenate str (not "int") to str
>>> name+'5'
'michael5'
>>> name*5
'michaelmichaelmichaelmichaelmichael'
>>> #hello
>>> name*
SyntaxError: invalid syntax
>>> name*3  #comment
'michaelmichaelmichael'
>>> for word in words:
	print(word)
	quit()

	
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    for word in words:
NameError: name 'words' is not defined
>>> bad name=5
SyntaxError: invalid syntax
>>> bad guy=1
SyntaxError: invalid syntax
>>> bad_guy=1
>>> bad1guy=1
>>> 1bad=2
SyntaxError: invalid syntax
>>> bad1@=1
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    bad1@=1
NameError: name 'bad1' is not defined
>>> abd1=1
>>> a=01
SyntaxError: invalid token
>>> 1.0/2.0*pi
1.57079632679
>>> name=input('Enter your name:\n')
Enter your name:
Chuck
>>> print('Hello'+name)
HelloChuck
>>> print('Hello 'name)
SyntaxError: invalid syntax
>>> print('Hello '+name)
Hello Chuck
>>> 'Hello '+name
'Hello Chuck'
>>> hours=input('Enter Hours:\n');
Enter Hours:
35
>>> rate=input('Enter Rate:\n')
Enter Rate:
2.75
>>> print('Pay: '+hours*rate)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    print('Pay: '+hours*rate)
TypeError: can't multiply sequence by non-int of type 'str'
>>> print('Pay: %f',hours*rate)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    print('Pay: %f',hours*rate)
TypeError: can't multiply sequence by non-int of type 'str'
>>> print('Pay: 'hours*rate)
SyntaxError: invalid syntax
>>> print('Pay: '+str(hours*rate))
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    print('Pay: '+str(hours*rate))
TypeError: can't multiply sequence by non-int of type 'str'
>>> hours*rate
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    hours*rate
TypeError: can't multiply sequence by non-int of type 'str'
>>> hours
'35'
>>> rate
'2.75'
>>> int(hours)
35
>>> hours
'35'
>>> print('Pay: '+int(hours)*int(rate))
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    print('Pay: '+int(hours)*int(rate))
ValueError: invalid literal for int() with base 10: '2.75'
>>> int(hours)*int(rate)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    int(hours)*int(rate)
ValueError: invalid literal for int() with base 10: '2.75'
>>> int(hours*rate)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    int(hours*rate)
TypeError: can't multiply sequence by non-int of type 'str'
>>> h=int(hours)
>>> r=int(rate)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    r=int(rate)
ValueError: invalid literal for int() with base 10: '2.75'
>>> r=float(rate)
>>> h*r
96.25
>>> print('Pay: '+h*r)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    print('Pay: '+h*r)
TypeError: can only concatenate str (not "float") to str
>>> print('Pay: 'h*r)
SyntaxError: invalid syntax
>>> 'h*r'
'h*r'
>>> h*r
96.25
>>> 'Pay: '+str(h*r)
'Pay: 96.25'
>>> print('Pay: '+str(h*r))
Pay: 96.25
>>> width = 17
>>> height = 12.0
>>> width//2
8
>>> width/2.0
8.5
>>> height/3
4.0
>>> 1+2*5
11
>>> raw_input
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    raw_input
NameError: name 'raw_input' is not defined
>>> 

>>> 
