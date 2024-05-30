PS C:\Users\Laptop\Documents\pythonlearning> python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> tea_types=("Black","Green","Oolong") ) 
  File "<stdin>", line 1
    tea_types=("Black","Green","Oolong") )
                                         ^
SyntaxError: unmatched ')'
>>> tea_types=("Black","Green","Oolong")  
>>> tea_types                              
('Black', 'Green', 'Oolong')
>>> tea_types[0]
'Black'
>>> tea_types[-1]
'Oolong'
>>> tea_types[1:]
('Green', 'Oolong')
>>> tea_types[0]="Lemon"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> len(tea_types)
3
>>> more_tea=("Herbal","Earl Grey")
>>> all_tea=more_tea+tea_types
>>> all_tea
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
>>> if "Green" in all_tea:
...  print("I have Green Tea")
...
I have Green Tea
>>> more_tea=("Herbal","Earl Grey","Herbal")
>>> more_tea.count("Herbal")                
2
>>> more_tea.count("Herb")   
0
>>> tea_types            
('Black', 'Green', 'Oolong')
>>> (black,green,Oolong)=tea_types
>>> black
'Black'
>>> type (tea_types)
<class 'tuple'>
>>> #Nesting is allowed in tuple