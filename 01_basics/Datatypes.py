# 1. String
username = "Bishesh"
print(username)  # Output: 'Bishesh'
username = "Marasini"
print(username)  # Output: 'Marasini'

# 2. Integer
x = 10
y = x  # y is a reference to x
print(x)  # Output: 10
print(y)  # Output: 10
x = 15  # Changing x does not affect y
print(y)  # Output: 10

# 3. List
mylist = [1, 2, 3, ['a', 'b']]  # List with mixed data types
print(len(mylist))  # Output: 4

# 4. Basic Operations
print(12 + 12)  # Output: 24
print(2.5 * 5)  # Output: 12.5
print(2 ** 100)  # Output: 1267650600228229401496703205376

# 5. Import math Module
import math
print(math.pi)  # Output: 3.141592653589793

# 6. Import random Module
import random
print(random.random())  # Output: A random float between 0 and 1
print(random.choice([1, 2, 3, 4, 5, 6]))  # Output: A random element from the list

# 7. String Operations
username = "chaiaurcode"
print(len(username))  # Output: 11
print(username[0])  # Output: 'c'
print(username[-1])  # Output: 'e'
print(username[-2])  # Output: 'd'
print(username[1:3])  # Output: 'ha'
print(dir(username))  # Output: List of string methods

# 8. List with Mixed Data Types
mylist = [123, "chai", 3.14]
print(mylist)  # Output: [123, 'chai', 3.14]
print(len(mylist))  # Output: 3
print(mylist[0])  # Output: 123
print(mylist[-1])  # Output: 3.14

# 9. Dictionary
myD = {'one': 'lemon', 'two': 'ginger', 'superman': 'ironman'}
print(myD)  # Output: {'one': 'lemon', 'two': 'ginger', 'superman': 'ironman'}
print(myD['superman'])  # Output: 'ironman'
print(myD['comic'])  # KeyError: 'comic'

# 10. Tuple
myTup = (1, 2, 4)
print(myTup[0])  # Output: 1
print(len(myTup))  # Output: 3

# 11. Import sys Module
import sys
print(sys.getrefcount(24601))  # Output: 3
print(sys.getrefcount('bishesh'))  # Output: 4294967295

# 12. Reassigning Variables
a = 3
a = "chaiaurcode"
a = 3.14
a = 5
b = 2
print(a)  # Output: 5
print(b)  # Output: 2
a = a + 2
print(a)  # Output: 7

# 13. Mutable and Immutable Objects
myListOne = [1, 2, 3]
myListTwo = myListOne  # Both reference the same list
myListOne = 'chai'  # myListOne now refers to a new string object
print(myListTwo)  # Output: [1, 2, 3]
myListOne = [1, 2, 3]  # Reassigning myListOne to a new list
print(myListTwo)  # Output: [1, 2, 3]
print(myListOne)  # Output: [1, 2, 3]
myListOne[0] = 33  # Modifying the list through myListOne
print(myListOne)  # Output: [33, 2, 3]
myListOne[0] = 70
print(myListOne)  # Output: [70, 2, 3]
print(myListTwo)  # Output: [70, 2, 3] (Affected by the change)

# 14. Shallow Copy
l1 = [1, 2, 3]
l2 = l1  # l2 is a reference to l1
print(l1)  # Output: [1, 2, 3]
print(l2)  # Output: [1, 2, 3]
l1[0] = 75  # Modifying l1 affects l2
print(l2)  # Output: [75, 2, 3]
print(l1)  # Output: [75, 2, 3]

# 15. Shallow Copy vs. Deep Copy
p1 = [1, 2, 3]
p2 = p1  # p2 is a reference to p1
p2 = [1, 2, 3]  # p2 now refers to a new list
p1[0] = 77  # Modifying p1
print(p1)  # Output: [77, 2, 3]
print(p2)  # Output: [1, 2, 3] (p2 is not affected)

h1 = [1, 2, 3]
h2 = h1[:]  # Shallow copy using slice
print(h1)  # Output: [1, 2, 3]
print(h2)  # Output: [1, 2, 3]
h1[0] = 78  # Modifying h1
print(h1)  # Output: [78, 2, 3]
print(h2)  # Output: [1, 2, 3] (h2 is not affected)

import copy
h2 = copy.copy(h1)  # Shallow copy
h2 = copy.deepcopy(h1)  # Deep copy

# 16. Comparing Objects
n = [1, 2, 3]
m = n
print(m)  # Output: [1, 2, 3]
print(n)  # Output: [1, 2, 3]
print(m == n)  # Output: True
print(m is n)  # Output: True

n = [1, 2, 3]
print(m == n)  # Output: True
print(m is n)  # Output: False