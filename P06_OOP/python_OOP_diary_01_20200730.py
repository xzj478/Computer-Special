Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> stuff = list()
>>> stuff.append('python')
>>> stuff.append('chuck')
>>> stuff.sort()
>>> print(stuff[0])
chuck
>>> print(stuff.__getitem__(0))
chuck
>>> print(list.__getitem__(stuff,0))
chuck
>>> stuff = list()
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> usf = input('Enter the US Floor Number: ')
Enter the US Floor Number: 13
>>> wf = int(usf)-1
>>> print('Non-US Floor Number is ', wf)
Non-US Floor Number is  12
>>> import urllib.request, urllib.parse, urllib.error
>>> from bs4 import BeautifulSoup
>>> import ssl
>>> ctx = ssl.create_default_context()
>>> ctx.check_hostname = False
>>> ctx.verify_mode = ssl.CERT_NONE
>>> url = input('Enter - ')
Enter - google
>>> html = urllib.request.urlopen(url, context=ctx).read()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    html = urllib.request.urlopen(url, context=ctx).read()
  File "D:\Python\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "D:\Python\lib\urllib\request.py", line 509, in open
    req = Request(fullurl, data)
  File "D:\Python\lib\urllib\request.py", line 328, in __init__
    self.full_url = url
  File "D:\Python\lib\urllib\request.py", line 354, in full_url
    self._parse()
  File "D:\Python\lib\urllib\request.py", line 383, in _parse
    raise ValueError("unknown url type: %r" % self.full_url)
ValueError: unknown url type: 'google'
>>> url = input('Enter - ')
Enter - https://www.google.com/
>>> html = urllib.request.urlopen(url, context=ctx).read()
>>> soup = BeautifulSoup(html, 'html.parser')
>>> tags = soup('a')
>>> for tag in tags:
	print(tag.get('href', None))

	
https://www.google.lv/imghp?hl=lv&tab=wi
https://maps.google.com/maps?hl=lv&tab=wl
https://www.youtube.com/?gl=LV&tab=w1
https://news.google.lv/nwshp?hl=lv&tab=wn
https://mail.google.com/mail/?tab=wm
https://drive.google.com/?tab=wo
https://www.google.com/calendar?tab=wc
https://www.google.lv/intl/lv/about/products?tab=wh
http://www.google.lv/history/optout?hl=lv
/preferences?hl=lv
https://accounts.google.com/ServiceLogin?hl=lv&passive=true&continue=https://www.google.com/
/advanced_search?hl=lv&authuser=0
https://www.google.com/setprefs?sig=0_SQ05iJ5xLJr-uZNKJ4lCjuGulKA%3D&hl=lt&source=homepage&sa=X&ved=0ahUKEwj32rPskPXqAhV15-AKHeFqCyYQ2ZgBCAU
https://www.google.com/setprefs?sig=0_SQ05iJ5xLJr-uZNKJ4lCjuGulKA%3D&hl=ru&source=homepage&sa=X&ved=0ahUKEwj32rPskPXqAhV15-AKHeFqCyYQ2ZgBCAY
http://www.google.lv/intl/lv/ads/
http://www.google.lv/intl/lv/services/
/intl/lv/about.html
https://www.google.com/setprefdomain?prefdom=LV&prev=https://www.google.lv/&sig=K_StfPL59WvUc1bIDQgdDPX4csJl0%3D
/intl/lv/policies/privacy/
/intl/lv/policies/terms/
>>> class PartyAnimal:
	x = 0

	
>>> class PartyAnimal:
	x = 0
	def party(self):
		self.x += 1
		print('So far',self.x)

		
>>> an = PartyAnimal()
>>> an.party()
So far 1
>>> an.party()
So far 2
>>> an.party()
So far 3
>>> PartyAnimal.party(an)
So far 4
>>> count = dict()
>>> an.party()
So far 5
>>> self.x += 1
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    self.x += 1
NameError: name 'self' is not defined
>>> PartyAnimal.party(an)
So far 6
>>> print('Type', type(an))
Type <class '__main__.PartyAnimal'>
>>> print('Dir', dir(an))
Dir ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'party', 'x']
>>> print('Type', type(an.x))
Type <class 'int'>
>>> print('Type', type(an.party))
Type <class 'method'>
>>> class PartyAnimal:
	x = 0
	def __init__(self):
		print('I am constructed')
	def party(self):
		self.x += 1
		print('So far',self.x)
	def __del__(self):
		print('I am destructed', self.x)

		
>>> an = PartyAnimal()
I am constructed
>>> an.party()
So far 1
>>> an.party()
So far 2
>>> an = 42
I am destructed 2
>>> print('an contains', an)
an contains 42
>>> class PartyAnimal:
	x = 0
	name = ''
	def __init__(self, nam):
		self.name = nam
		print(self.name, 'constructed')
	def party(self):
		self.x += 1
		print(self.name, 'party count',self.x)

		
>>> s = PartyAnimal('Sally')
Sally constructed
>>> j = PartyAnimal('Jim')
Jim constructed
>>> s.party()
Sally party count 1
>>> j.party()
Jim party count 1
>>> s.party()
Sally party count 2
>>> from party import PartyAnimal
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    from party import PartyAnimal
ModuleNotFoundError: No module named 'party'
>>> class CricketFan(PartyAnimal):
	points = 0
	def six(self):
		self.points += 6
		self.party()
		print(self.name,'points',self.points)

		
>>> s = PartyAnimal('Sally')
Sally constructed
>>> s.party()
Sally party count 1
>>> j = CricketFan('Jim')
Jim constructed
>>> j.party()
Jim party count 1
>>> j.six()
Jim party count 2
Jim points 6
>>> print(dir(j))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'party', 'points', 'six', 'x']
>>> 