Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(32)
<class 'int'>
>>> max('Hello World')
'r'
>>> min('Hello World')
' '
>>> len('Hello World')
11
>>> int('32')
32
>>> int('Hello')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int('Hello')
ValueError: invalid literal for int() with base 10: 'Hello'
>>> int(3.99)
3
>>> int(-2.9)
-2
>>> float(32)
32.0
>>> float('3.14159265358')
3.14159265358
>>> import math
>>> print(math)
<module 'math' (built-in)>
>>> ratio = signal_power / noise_power
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ratio = signal_power / noise_power
NameError: name 'signal_power' is not defined
>>> radians = 0.7
>>> height = math.sin(radians)
>>> height
0.644217687237691
#
>>> pi
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
>>> pi=3.14
>>> sin(pi)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    sin(pi)
NameError: name 'sin' is not defined
>>> math.sin(pi)
0.0015926529164868282
>>> math.sin(pi/2)
0.9999996829318346
>>> degrees=45
>>> radians=degrees/360*2*math.pi
>>> math.sin(radians)
0.7071067811865476
>>> math.sin(math.pi)
1.2246467991473532e-16
>>> math.sin(math.pi/2)
1.0
>>> math.sqrt(2)
1.4142135623730951
>>> import random
>>> for i in range(10):
	x=random.random()
	print(x)

	
0.716023690923446
0.03495493902812863
0.43554744596574024
0.26647880044636196
0.8931822025889498
0.02095574624534946
0.9617064081681256
0.30515311874669626
0.6167052583181082
0.6770123073312858
>>> random.randint(5,10)
10
>>> random.randint(0,100)
51
>>> random.randint(0,100)
32
>>> def print_lyrics():
	print('I love you and Im fine.')
	print("Good morning world.")

	
>>> print(print_lyrics)
<function print_lyrics at 0x0000026957389A60>
>>> type(print_lyrics)
<class 'function'>
>>> print_lyrics
<function print_lyrics at 0x0000026957389A60>
>>> print_lyrics()
I love you and Im fine.
Good morning world.
>>> def repeat_lyrics():
	for i in range(10):
		print_lyrics()

		
>>> repeat_lyrics()
I love you and Im fine.
Good morning world.
I love you and Im fine.
Good morning world.
I love you and Im fine.
Good morning world.
I love you and Im fine.
Good morning world.
I love you and Im fine.
Good morning world.
I love you and Im fine.
Good morning world.
I love you and Im fine.
Good morning world.
I love you and Im fine.
Good morning world.
I love you and Im fine.
Good morning world.
I love you and Im fine.
Good morning world.
>>> def print_twice(bruce):
	print(bruce)
	print(bruce)

	
>>> print_twice('Hello')
Hello
Hello
>>> print_twice(17)
17
17
>>> math
<module 'math' (built-in)>
>>> print_twice(math.pi)
3.141592653589793
3.141592653589793
>>> result
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    result
NameError: name 'result' is not defined
>>> None
>>> print(result)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(result)
NameError: name 'result' is not defined
>>> print(type(None))
<class 'NoneType'>
>>> def addtwo(a,b):
	added = a + b
	return added

>>> addtwo(3,5)
8
>>> 
