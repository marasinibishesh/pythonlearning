>>> x=2
>>> y=3
>>> z=4
>>> x+y
5
>>> x+y*z
14
>>> # this is not good
>>> (x+y)*z #write in parenthesis for more code readability
20
>>> x+(y*z)
14
>>> 40+2.23 #code is write but always focus for both datatype value same
42.23
>>> 'bishesh'+3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> int(2.23)
2
>>> float(40)
40.0
>>> #this is a good approach    
>>> 'chai'+'code'
'chaicode'
>>> x,y,z
(2, 3, 4)
>>> x+1,y*2 
(3, 6)
>>> y%2
1
>>> z**2 #for power
16
>>> 100**2
10000
>>> 2*100
200
>>> 2**100
1267650600228229401496703205376
>>> 2*1000
2000
>>> 2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>> result=1/3.0
>>> result
0.3333333333333333
>>> repr('chai')
"'chai'"
>>> str('chai')
'chai'
>>> print('chai')
chai
>>> #comparision
>>> 1<2  
True
True
>>> # integer divide
>>> 22//7
3
>>> 22/7
3.142857142857143
>>> #comparision
>>> 5.0==5.0
True
>>> 4.0 !=5.0
True
>>> x,y,z
(2, 3, 4)
>>> x<y<z
True
>>> x<y and y<z
True
>>> #both statements are true but prefer using second one
>>> 1==2<3
False
>>> 1==2 and 2 < 3
False
>>> #both statements are true but prefer using second one
>>> import math
>>> math.floor(3.5)
3
>>> math.ceil(3.5)
4
>>> math.floor(-3.5)
-4
>>> math.ceil(-3.5)
-3
>>> math.trunc(2.8) # takes towards zero
2
>>> math.trunc(-2.8)
-2
>>> 9999999999999999999999999999999999999999 + 1
10000000000000000000000000000000000000000
>>> 2*200                                           
400
>>> 2**200
1606938044258990275541962092341162602522202993782792835301376
>>> # handling complex number
>>> 2+1j  
(2+1j)
>>> 2+1j*3
(2+3j)
>>> (2+1j)*3
(6+3j)
>>> 0o20
16
>>> #0o for defining octal number
>>> #0xFF
>>> 0xff
255
>>> #0xFF for hexadecimal
>>> oct(64)
'0o100'
>>>
>>>
>>> hex(64)
'0x40'
>>> int(3.14)
3
>>> int('64',8)
52
>>> #for converting in octal
>>> int('64',16)
100
>>> #for converting in hexadecimal
>>> x=1
>>> x<<2
4
>>> import random
>>> random.random()
0.7644766794550082
>>> random.randint(1,10) 
3
>>> random.randint(1,10)
2
>>> random.randint(1,10)
5
>>> random.randint(1,10)
4
>>> random.random()      
0.7979526747963328
>>> random.randint(1,10)
9
>>> random.randint(1,10)
1
>>> random.randint(1,10)
10
>>> l1=['lemon','masala','ginger','mint']
>>> random.choice(l1)
'lemon'
>>> random.choice(l1)
'masala'
>>> random.choice(l1)
'lemon'
>>> random.choice(l1)
'masala'
>>> random.shuffle(l1)
>>> l1                
['masala', 'ginger', 'mint', 'lemon']
>>> l1
['masala', 'ginger', 'mint', 'lemon']
>>> random.shuffle(l1)
>>> random.shuffle(l1)
>>> l1
['masala', 'lemon', 'ginger', 'mint']
>>> 0.1+0.1+0.4
0.6000000000000001
>>> (0.1+0.1+0.1)-0.3
5.551115123125783e-17
>>> from decimal import decimal
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'decimal' from 'decimal' (C:\Users\Laptop\AppData\Local\Programs\Python\Python312\Lib\decimal.py). Did you mean: 'Decimal'?
>>> Truw
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Truw' is not defined. Did you mean: 'True'?
>>> Truw
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Truw' is not defined. Did you mean: 'True'?
>>> True
True
>>> from decimal import  Decimal
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')+Decimal('0.3')
Decimal('0.6')
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3') 
Decimal('0.0')
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
Decimal('0.0')
>>> from fraction import Fraction
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'fraction'
>>> from fractions import Fraction
>>> myFra=Fraction(2,7)
>>> myFra
Fraction(2, 7)
>>> setone={1,2,3,4 }
>>> setone & {1,3}
{1, 3}
>>> #for intersection
>>> setone | {1,3}
{1, 2, 3, 4}
>>> #for union
>>> setone-{1,2,3,4}
set()
>>> type({})
<class 'dict'>
>>> #use type() for checking typeof
>>> type?(True)
  File "<stdin>", line 1
    type?(True)
        ^
SyntaxError: invalid syntax
>>> type(True)
<class 'bool'>
>>> True==1
True
>>> False==0
True
>>> True is 1
<stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False