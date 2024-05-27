PS C:\Users\Laptop\Documents\pythonlearning\01_basics> python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import hello_world
Bishesh and Dark
Bishesh and Bright
>>> hello_world.biscal("Bishesh is hero")
Bishesh is hero
>>> import hello_chai.chai_one
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'hello_chai'
>>> from importlib import reload
>>> reload(hello_world)
Bishesh and Dark
Bishesh and Bright
<module 'hello_world' from 'C:\\Users\\Laptop\\Documents\\pythonlearning\\01_basics\\hello_world.py'>       
>>> import hello_chai.chai_one
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'hello_chai'
>>> import hello_world.chai_one
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'hello_world.chai_one'; 'hello_world' is not a package
>>> from importlib import reload
>>> reload(hello_world)
Bishesh and Dark
Bishesh and Bright
<module 'hello_world' from 'C:\\Users\\Laptop\\Documents\\pythonlearning\\01_basics\\hello_world.py'>       
>>> hello_world.chai_one
'lemon tea'
>>> ^Z

PS C:\Users\Laptop\Documents\pythonlearning\01_basics> python 01_basics/hello_world.py
C:\Users\Laptop\AppData\Local\Programs\Python\Python312\python.exe: can't open file 'C:\\Users\\Laptop\\Documents\\pythonlearning\\01_basics\\01_basics\\hello_world.py': [Errno 2] No such file or directory
PS C:\Users\Laptop\Documents\pythonlearning\01_basics> git add .
PS C:\Users\Laptop\Documents\pythonlearning\01_basics> git commit -m"Python Internal Strucutre Foundation"
[main 28f7f52] Python Internal Strucutre Foundation
 3 files changed, 12 insertions(+)
 create mode 100644 01_basics/__pycache__/hello_world.cpython-312.pyc
 create mode 100644 01_basics/hello_world.py
 create mode 100644 01_basics/world.py
PS C:\Users\Laptop\Documents\pythonlearning\01_basics> git push
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (7/7), 1.04 KiB | 1.04 MiB/s, done.
Total 7 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/marasinibishesh/pythonlearning.git
   3f39652..28f7f52  main -> main
PS C:\Users\Laptop\Documents\pythonlearning\01_basics> python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> username = "Bishesh"
>>> username
'Bishesh'
>>> username="Marasini"
>>> username
'Marasini'
>>> x=10
>>> y=x
>>> x
10
>>> y
10
>>> x=15
>>> y
10
>>> y
10
>>>
 *  History restored 

PS C:\Users\Laptop\Documents\pythonlearning\01_basics> python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> mylist=[1,2,3,['a','b']]
>>> 12+12
24
>>> 2.5*5
12.5
>>> 2 ** 100
1267650600228229401496703205376
>>> import math
>>> math.pi
3.141592653589793
>>> import random
>>> random.random()
0.8020300713078639
>>> random.choice([1,2,3,4,5,6])
6
>>> random.choice([1,2,3,4,5,6])
6
>>> random.choice([1,2,3,4,5,6])
3
>>> random.choice([1,2,3,4,5,6])
1
>>> random.choice([1,2,3,4,5,6])
3
>>> random.choice([1,2,3,4,5,6])
3
>>> random.choice([1,2,3,4,5,6])
3
>>> random.choice([1,2,3,4,5,6])
1
>>> random.choice([1,2,3,4,5,6])
1
>>> random.choice([1,2,3,4,5,6])
2
>>> random.choice([1,2,3,4,5,6])
3
>>> random.choice([1,2,3,4,5,6])
3
>>> random.choice([1,2,3,4,5,6])
4
>>> username="chaiaurcode 
  File "<stdin>", line 1
    username="chaiaurcode
             ^
SyntaxError: unterminated string literal (detected at line 1)
>>> username="chaiaurcode"
>>> len(username)
11
>>> username[0]
'c'
>>> username[-1]
'e'
>>> username[-2]
'd'
>>> username[1:3]
'ha'
>>> dir(username)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> mylist=[123,"chai",3.14]
>>> mylist
[123, 'chai', 3.14]
>>> len(mylist)
3
>>> mylist[0]
123
>>> mylist[0]
123
>>> mylist[-1]
3.14
>>> len(mylist)
3
>>> myD={'one':'lemon','two':'ginger','superman':'ironman'}
>>> myD
{'one': 'lemon', 'two': 'ginger', 'superman': 'ironman'}
>>> myD['comic']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'comic'
>>> myD['superman']
'ironman'
>>> myTup=(1,2,4)
>>> myTup[0]
1
>>> len(myTup)
3
>>> import sys
>>> sys.getrefcount(24601)  
3
>>> sys.getrefcount('bishesh')
4294967295
>>> a=3
>>> a="chaiaurcode'
  File "<stdin>", line 1
    a="chaiaurcode'
      ^
SyntaxError: unterminated string literal (detected at line 1)
>>> a="chaiaurcode"
>>> a=3.14
>>> a=5
>>> b=2
>>> a
5
>>> b
2
>>> a=a+2
>>> a
7
>>> myListOne=[1,2,3]
>>> myListTwo=myListOne
>>> myListOne='chai'
>>> myListTwo
[1, 2, 3]
>>> myListOne=[1,2,3]
>>> myListTwo
[1, 2, 3]
>>> myListOne       
[1, 2, 3]
>>> myListOne
[1, 2, 3]
>>> myListOne[0]=33
>>> myListOne       
[33, 2, 3]
>>> myListOne[0]=70
>>> myListOne       
[70, 2, 3]
>>> myListTwo
[1, 2, 3]
>>> l1=[1,2,3]
>>> l2=l1
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
>>> l1[0]=75
>>> l2      
[75, 2, 3]
>>> l1
[75, 2, 3]
>>> p1=[1,2,3]
>>> p2=p1
>>> p2=[1,2,3]
>>> p1[0]=77
>>> p1
[77, 2, 3]
>>> p2
[1, 2, 3]
>>> h1=[1,2,3]
>>> h2=h1[:]  
>>> h1
[1, 2, 3]
>>> h2
[1, 2, 3]
>>> h1[0]=78
>>> h1       
[78, 2, 3]
>>> h2
[1, 2, 3]
>>> import copy
>>> h2=copy.copy(h1)
>>> h2=copy.deepcopy(h1)
>>> n=[1,2,3]
>>> m=n
>>> m
[1, 2, 3]
>>> n
[1, 2, 3]
>>> m==n
True
>>> m is n
True
>>> n=[1,2,3]
>>> m==n
True
>>> m is n
False
>>>