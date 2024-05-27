>>>num_list=[0,1,2,3,4,5,6,7,8,9]
>>> num_list[:]
'0123456789'
>>> num_list[0:]
'0123456789'
>>> num_list[:7]
'0123456'
>>> num_list[0:7:2]
'0246'
>>> num_list[0:7:3]
'036'
>>> num_list[0:7:-1]
''
>>> num_list[0:-1]  
'012345678'
>>> chai
'Masala Chai'
>>> print(chai.lower())
masala chai
>>> print(chai.upper())
MASALA CHAI
>>> chai="   Masala Chai   "
>>> chai
'   Masala Chai   '
>>> print(chai.strip)
<built-in method strip of str object at 0x0000025B9A446E70>
>>> print(chai.strip())
Masala Chai
>>> chai="lemon chai"
>>> print(chai.replace("lemon","Masala"))
Masala chai
>>>
>>> chai="lemon,Ginger,Masala,Mint"
>>> print(chai.split(", "))
['lemon,Ginger,Masala,Mint']
>>> chai="Masala Chai"
>>> print(chai.find("Chai")
... print(chai.find("Chai"))
  File "<stdin>", line 1
    print(chai.find("Chai")
          ^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(chai.find("Chai"))
7
>>> print(chai.find("chai")) 
-1
>>> chai="Masala Chai Chai Chai"
>>> print(chai.count("Chai"))
3
>>> chai_type="Masala"
>>> quantity=2
>>> order="I ordered {} cups of {} chai"
>>>  print(order.format(quantity,chai_type))
  File "<stdin>", line 1
    print(order.format(quantity,chai_type))
IndentationError: unexpected indent
>>>  print(order.format(quantity,chai_type))
  File "<stdin>", line 1
    print(order.format(quantity,chai_type))
IndentationError: unexpected indent
>>> order='I ordered {} cups of {} chai'     
>>>  print(order.format(quantity,chai_type))
  File "<stdin>", line 1
    print(order.format(quantity,chai_type))
IndentationError: unexpected indent
>>>  print(order.format(quantity, chai_type))
  File "<stdin>", line 1
    print(order.format(quantity, chai_type))
IndentationError: unexpected indent
>>> chai_type="Masala"                        
>>> quantity=2
>>> order="I ordered {} cups of {} chai"
>>>  print(order.format(quantity, chai_type))
  File "<stdin>", line 1
    print(order.format(quantity, chai_type))
IndentationError: unexpected indent
>>> order='I ordered {} cups of {} chai'      
>>> order                                     
'I ordered {} cups of {} chai'
>>>  print(order.format(quantity, chai_type))
  File "<stdin>", line 1
    print(order.format(quantity, chai_type))
IndentationError: unexpected indent
>>>   print(order.format(quantity, chai_type))
  File "<stdin>", line 1
    print(order.format(quantity, chai_type))
IndentationError: unexpected indent
>>>   print(order.format(quantity)            
  File "<stdin>", line 1
    print(order.format(quantity)
IndentationError: unexpected indent
>>> chai_type= "Masala"                        
>>> quantity= 2                                
>>> order= "I ordered {} cups of {} chai"      
>>> order
'I ordered {} cups of {} chai'
>>>   print(order.format(quantity, chai_type))
  File "<stdin>", line 1
    print(order.format(quantity, chai_type))
IndentationError: unexpected indent
>>>
KeyboardInterrupt
>>> chai_type="Masala"                         
>>> quantity=2                                
>>> chai="Masala Chai Chai Chai" 
>>> order="I ordered {} cups of {} chai"  
>>> print(order.format(quantity, chai_type)) 
I ordered 2 cups of Masala chai
>>> #coverting list to string code
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> #coverting list to string code
>>>
>>>
>>>
>>>
>>>
>>> #coverting list to string code
>>>
 *  History restored 

PS C:\Users\Laptop\Documents\pythonlearning> python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> chai_variety=["lemon", "Masala", "Ginger"]
>>> chai_variety
['lemon', 'Masala', 'Ginger']
>>> print("".join(chai_variety))
lemonMasalaGinger
>>> chai=" ".join(chai_variety)       
>>> chai
'lemon Masala Ginger'
>>> chai=",  ".join(chai_variety)
>>> chai
'lemon,  Masala,  Ginger'
>>> chai="- ".join(chai_variety)) 
  File "<stdin>", line 1
    chai="- ".join(chai_variety))
                                ^
SyntaxError: unmatched ')'
>>> chai="-".join(chai_variety))) 
  File "<stdin>", line 1
    chai="-".join(chai_variety)))
                               ^
SyntaxError: unmatched ')'
>>> chai=",  ".join(chai_variety)
>>> chai="- ".join(chai_variety)  
>>> chai=",  ".join(chai_variety)
>>> chai="-".join(chai_variety))) 
  File "<stdin>", line 1
    chai="-".join(chai_variety)))
                               ^
SyntaxError: unmatched ')'
>>> chai="- ".join(chai_variety)  
>>> chai=",  ".join(chai_variety)
>>> chai="- ".join(chai_variety)  
>>> chai=",  ".join(chai_variety)
>>> chai
'lemon,  Masala,  Ginger'
>>> chai="- ".join(chai_variety)  
>>> chai
'lemon- Masala- Ginger'
>>> chai
'lemon- Masala- Ginger'
>>> chai="Masala Chai"
>>> print(len(chai))
11
>>> chai
'Masala Chai'
>>> for letter in chai:
...  print(letter)
...
M
a
s
a
l
a

C
h
a
i
>>> #for printing individual letter
>>> for letter in chai:
...  print(letter)
...
M
a
s
a
l
a

C
h
a
i
>>> chai="He said,"Masala chai is awesome""
  File "<stdin>", line 1
    chai="He said,"Masala chai is awesome""
                   ^^^^^^
SyntaxError: invalid syntax
>>> chai="He said,\"Masala chai is awesome\""
>>> chai
'He said,"Masala chai is awesome"'
>>> chai="Masala\nchai"
>>> chai
'Masala\nchai'
>>> print(chai)
Masala
chai
>>> chai=r"Masala\nChai"
>>> print(chai) 
Masala\nChai
>>> chai=r"c:\user\pwd"
>>> print(chai)
c:\user\pwd
>>> chai="Masala Chai"
>>> print("Masala" in chai)
True
>>> print("Masalaa" in chai)
False