Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============================== RESTART: Shell ===============================
>>> 5==5
True
>>> 5==6
False
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> 1!=2
True
>>> 1>2
False
>>> 1<2
True
>>> 1 is 2
False
>>> 1 is 1
True
>>> 1 is not 1
False
>>> 17 and True
True
>>> 0 and True
0
>>> -1 and True
True
>>> 0 and 17
0
>>> 0 and 0
0
>>> 1 and 17
17
>>> 2 and 3
3
>>> True and 2
2
>>> True and False
False
>>> True or False
True
>>> x = 0
>>> if x>0:
	print('x is positive')

	
>>> x=0
>>> if x<0:
	pass

>>> x=7
>>> if x>0:
	print('Hello '+str(x))

	
Hello 7
>>> if x%2==0:
	print('x is even')
	else:
		
SyntaxError: invalid syntax
>>> if x%2==0:
	print('x is even')
else:
	print('x is odd')

	
x is odd
>>> y=11
>>> if x<y:
	print('x is less than y')
elif x>y:
	print('x is greater than y')
else:
	print('x and y are equal')

	
x is less than y
>>> choice = a
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    choice = a
NameError: name 'a' is not defined
>>> choice = 'a'
>>> if choice == 'a':
	print('Bad guess')
elif:
	
SyntaxError: invalid syntax
>>> if choice == 'a':
	print('Bad guess')
elif choice == 'b':
	print('Good guess')
elif choice == 'c':
	print('Close, but not correct')

	
Bad guess
>>> if x>0:
	if x<10:
		print('x is a positive single-digit number.')

		
x is a positive single-digit number.
>>> if x>0 and x<10:
	print('x is a positive single-digit number')

	
x is a positive single-digit number
>>> pt = 'Enter Fahrenheit Temperature:'
>>> inp = input(pt)
Enter Fahrenheit Temperature:fred
>>> fahr = float(inp)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    fahr = float(inp)
ValueError: could not convert string to float: 'fred'
>>> try:
	fahr = float(inp)
	cel = (fahr - 32)*5/9
	print(cel)
except:
	print('Please enter a number')

	
Please enter a number
>>> try:
	fahr = float(inp)
	cel = (fahr - 32)*5/9
	print(cel)
except:
	print('Please enter a number')
	return
SyntaxError: 'return' outside function
>>> try:
	fahr = float(inp)
	cel = (fahr - 32)*5/9
	print(cel)
except:
	print('Please enter a number')
return
SyntaxError: invalid syntax
>>> x = 6
>>> 
