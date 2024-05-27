PS C:\Users\Laptop\Documents\pythonlearning> python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hello")
hello
>>> 2*2
4
>>> 3+5
8
>>> "chai"*4
'chaichaichaichai'
>>> score=100
>>> print(score)
100
>>> score
100
>>> tea
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tea' is not defined
>>> ^D
  File "<stdin>", line 1
    ♦
    ^
SyntaxError: invalid non-printable character U+0004
>>> import os
>>> os.getcwd()
'C:\\Users\\Laptop\\Documents\\pythonlearning'
>>> for c in "chai":
... print(c)
  File "<stdin>", line 2
    print(c)
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for c in "chai":
...  print(c)
...
c
h
a
i
>>> import sys
>>> sys.platform
'win32'
>>> ls
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ls' is not defined. Did you mean: 'os'?
>>> import hello_world
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'hello_world'
>>>
KeyboardInterrupt
>>>
 *  History restored 

PS C:\Users\Laptop\Documents\pythonlearning>



PS C:\Users\Laptop\Documents\pythonlearning>