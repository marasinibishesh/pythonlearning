PS C:\Users\Laptop\Documents\pythonlearning> python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> chai_types={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Masala"]
'Spicy'
>>> chai_types.get("Ginger")
'Zesty'
>>> chai_types.get("Gingery")
>>> chai_types["Gingery"]     
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Gingery'
>>> chai_types           
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Green"]=["Fresh"]
>>> chai_types                   
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': ['Fresh']}
>>> chai_types["Green"]="Fresh"  
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> #iteration
>>> for chai in chai_types:
...  print(chai)
...
Masala
Ginger
Green
>>> for chai in chai_types:
...  print(chai,chai_types[chai])
...
Masala Spicy
Ginger Zesty
Green Fresh
>>> for key,values  in chai_types:
... for key,values  in chai_types.items():
  File "<stdin>", line 2
    for key,values  in chai_types.items():
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for key,values  in chai_types.items():
...  print(key,values)
...
Masala Spicy
Ginger Zesty
Green Fresh
>>> for key,value  in chai_types.items():  
...  print(key,value) 
...
Masala Spicy
Ginger Zesty
Green Fresh
>>> if "Masala" in chai_types:
...  print("I have masala chai")
...
I have masala chai
>>> print(len(chai_types))
3
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> chai_types["Earl Grey"]="Citrus"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
>>> chai_types.pop("Ginger")
'Zesty'
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
>>> chai_types.popitem()
('Earl Grey', 'Citrus')
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh'}
>>> del chai_types["Green"]
>>> chai_types
{'Masala': 'Spicy'}
>>> chai_types_copy=chai_types.copy()
>>> tea_shop={
... "chai":{"Masala":"Spicy","Ginger":"Zesty"},
... "Tea":{"Green":"Fresh","Black":"Strong"}
... }
>>> tea_shop
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Fresh', 'Black': 'Strong'}}