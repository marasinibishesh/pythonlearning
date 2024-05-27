>>> tea_varities=["Black", "Green", "Oolong", "White"] 
>>> print(tea_varities)
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varities[0])
Black
>>> print(tea_varities[-1])
White
>>> print(tea_varities[1:3])
['Green', 'Oolong']
>>> print(tea_varities[:3])  
['Black', 'Green', 'Oolong']
>>> print(tea_varities[:2]) 
['Black', 'Green']
>>> print(tea_varities[2:])  
['Oolong', 'White']
>>> print(tea_varities[2:2])
[]
>>> tea_varities[3]="Herbal"
>>> print(tea_varities)      
['Black', 'Green', 'Oolong', 'Herbal']
>>> print(tea_varities[1:2])
['Green']
>>> tea_varities[1:2]="Lemon"  
>>> tea_varities)             
  File "<stdin>", line 1
    tea_varities)
                ^
SyntaxError: unmatched ')'
>>> tea_varities 
['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
>>> tea_varities=["Black", "Green", "Oolong", "White"]
>>> tea_varities[1:2]        
['Green']
>>> tea_varities[1:2]=["Lemon"]
>>> tea_varities
['Black', 'Lemon', 'Oolong', 'White']
>>> tea_varities[1:3]         
['Lemon', 'Oolong']
>>> tea_varities[1:3]=["Green","Masala"]
>>> tea_varities      
['Black', 'Green', 'Masala', 'White']
>>> print(tea_varities[2:2])
PS C:\Users\Laptop\Documents\pythonlearning> python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
 *  History restored 

PS C:\Users\Laptop\Documents\pythonlearning> python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> tea_varities=["Black", "Green", "Oolong", "White"]
>>> tea_varities
['Black', 'Green', 'Oolong', 'White']
>>> tea_varities[1:1]
[]
>>> tea_varities[1:1]=["test","test"]
>>> tea_varities[1:1]
[]
>>> tea_varities      
['Black', 'test', 'test', 'Green', 'Oolong', 'White']
>>> tea_varities[1:2]                
['test']
>>> tea_varities[1:3]
['test', 'test']
>>> tea_varities[1:3]=[] #deletion operation            
>>> tea_varities      
['Black', 'Green', 'Oolong', 'White']
>>> tea_varities[3]=["Masala"]
>>> tea_varities
['Black', 'Green', 'Oolong', ['Masala']]
>>> tea_varities[3]="Masala"  
>>> tea_varities
['Black', 'Green', 'Oolong', 'Masala']
>>> tea_varities=["Black", "Green", "Oolong", "White"]
>>> tea_varities[2]="Masala"  
>>> tea_varities
['Black', 'Green', 'Masala', 'White']
>>> for tea in tea_varities:
...     print(tea)
...
Black
Green
Masala
White
>>> for tea in tea_varities:
...     print(tea,end="-")
...
Black-Green-Masala-White->>> tea_varities
['Black', 'Green', 'Masala', 'White']
>>> if "Oolong" in tea_varities:
...     print("I have Oolong Tea")
...
>>> tea_varities.append("Oolong") #to add value at end of list
>>> tea_varities                                              
['Black', 'Green', 'Masala', 'White', 'Oolong']
>>> if "Oolong" in tea_varities:   
...     print("I have Oolong Tea")
...
I have Oolong Tea
>>> tea_varities.pop() #to remove last value
'Oolong'
>>> tea_varities                   
['Black', 'Green', 'Masala', 'White']
>>> tea_varities.remove("green") #to remove give value
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> tea_varities.remove(Green") #to remove give value         
  File "<stdin>", line 1
    tea_varities.remove(Green") #to remove give value
                             ^
SyntaxError: unterminated string literal (detected at line 1)
>>> tea_varities.remove("Green") #to remove give value
>>> tea_varities
['Black', 'Masala', 'White']
>>> tea_varities.insert(1,"green")
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>> tea_varities_copy=tea_varities.copy() #to seperate references
>>> tea_varities_copy                                            
['Black', 'green', 'Masala', 'White']
>>> tea_varities_copy.append("Lemon")
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>> tea_varities_copy
['Black', 'green', 'Masala', 'White', 'Lemon']
>>> f
 *  History restored 

PS C:\Users\Laptop\Documents\pythonlearning> python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #append() command is used to add something at end of list
>>> tea_varities_copy                                         
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tea_varities_copy' is not defined
>>> tea_varities
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tea_varities' is not defined
>>> #--------------------------------------------------
>>> squared_nums=[x**2 for x in range(10)]  
>>> range(10)
range(0, 10)
>>> print(range(0,10))
range(0, 10)
>>> y=range(10)
>>> y
range(0, 10)
>>> squared_nums=[x**2 for x in range(10)]
>>> squared_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube_nums=[y**3 for x in rage(10)]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rage' is not defined. Did you mean: 'range'?
>>> cube_nums=[y**3 for x in range(10)]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'range' and 'int'
>>> squared_nums=[x**2 for x in range(10)]
>>> squared_nums=[x**2 for x in range(10)]
>>> cube_nums=[y**3 for y in rage(10)] 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rage' is not defined. Did you mean: 'range'?
>>> cube_nums=[y**3 for y in range(10)]
>>> cube_nums
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>>