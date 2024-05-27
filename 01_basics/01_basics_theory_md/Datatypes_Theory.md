# Data Types in Python

Python has several built-in data types that are used to store and manipulate different kinds of data. In this file, we'll explore the following data types:

## 1. Strings

A string is a sequence of characters enclosed within single or double quotes. Here are some examples:

```python
username = "Bishesh"
print(username)  # Output: 'Bishesh'
username = "Marasini"
print(username)  # Output: 'Marasini'

username = "chaiaurcode"
print(len(username))  # Output: 11
print(username[0])  # Output: 'c'
print(username[-1])  # Output: 'e'
print(username[-2])  # Output: 'd'
print(username[1:3])  # Output: 'ha'
print(dir(username))  # Output: List of string methods
```

Strings are immutable, meaning they cannot be modified once created.

## 2. Integers

Integers are whole numbers (positive, negative, or zero) without fractional parts. Here's an example:

```python
x = 10
y = x  # y is a reference to x
print(x)  # Output: 10
print(y)  # Output: 10
x = 15  # Changing x does not affect y
print(y)  # Output: 10
```

## 3. Lists

Lists are ordered collections of items, which can be of different data types. Lists are mutable, meaning you can modify them after creation. Here's an example:

```python
mylist = [1, 2, 3, ['a', 'b']]  # List with mixed data types
print(len(mylist))  # Output: 4
mylist = [123, "chai", 3.14]
print(mylist)  # Output: [123, 'chai', 3.14]
print(len(mylist))  # Output: 3
print(mylist[0])  # Output: 123
print(mylist[-1])  # Output: 3.14
```

## 4. Dictionaries

Dictionaries are unordered collections of key-value pairs. Here's an example:

```python
myD = {'one': 'lemon', 'two': 'ginger', 'superman': 'ironman'}
print(myD)  # Output: {'one': 'lemon', 'two': 'ginger', 'superman': 'ironman'}
print(myD['superman'])  # Output: 'ironman'
print(myD['comic'])  # KeyError: 'comic'
```

## 5. Tuples

Tuples are ordered collections of items, similar to lists, but they are immutable, meaning they cannot be modified after creation. Here's an example:

```python
myTup = (1, 2, 4)
print(myTup[0])  # Output: 1
print(len(myTup))  # Output: 3
```

## 6. Mutable vs. Immutable Objects

Mutable objects can be modified after creation, while immutable objects cannot. Lists and dictionaries are mutable, while strings, integers, and tuples are immutable.

```python
myListOne = [1, 2, 3]
myListTwo = myListOne  # Both reference the same list
myListOne = 'chai'  # myListOne now refers to a new string object
print(myListTwo)  # Output: [1, 2, 3]
myListOne = [1, 2, 3]  # Reassigning myListOne to a new list
print(myListTwo)  # Output: [1, 2, 3]
print(myListOne)  # Output: [1, 2, 3]
myListOne[0] = 33  # Modifying the list through myListOne
print(myListOne)  # Output: [33, 2, 3]
```

## 7. Shallow Copy vs. Deep Copy

When you create a copy of a mutable object, you can choose between a shallow copy or a deep copy. A shallow copy creates a new reference to the original object, while a deep copy creates a new independent object with a copy of the original object's contents.

```python
import copy

# Shallow copy
l1 = [1, 2, 3]
l2 = l1  # l2 is a reference to l1
l1[0] = 75  # Modifying l1 affects l2
print(l2)  # Output: [75, 2, 3]

# Deep copy
h1 = [1, 2, 3]
h2 = copy.deepcopy(h1)  # Deep copy
h1[0] = 78  # Modifying h1
print(h1)  # Output: [78, 2, 3]
print(h2)  # Output: [1, 2, 3] (h2 is not affected)
```

## 8. Comparing Objects

You can compare objects using the `==` operator (for value equality) and the `is` operator (for identity check).

```python
n = [1, 2, 3]
m = n
print(m == n)  # Output: True
print(m is n)  # Output: True

n = [1, 2, 3]
print(m == n)  # Output: True
print(m is n)  # Output: False
```

In this file, we explored various data types in Python, including strings, integers, lists, dictionaries, and tuples. We also covered concepts like mutable vs. immutable objects, shallow and deep copies, and comparing objects. Understanding these data types and their behaviors is crucial for effective programming in Python.