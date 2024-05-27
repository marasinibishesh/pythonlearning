# Creating a list of tea varieties
tea_varieties = ["Black", "Green", "Oolong", "White"]
print(tea_varieties)
# Output: ['Black', 'Green', 'Oolong', 'White']

# Accessing list elements
print(tea_varieties[0])  # Output: Black
print(tea_varieties[-1]) # Output: White
print(tea_varieties[1:3]) # Output: ['Green', 'Oolong']
print(tea_varieties[:3])  # Output: ['Black', 'Green', 'Oolong']
print(tea_varieties[:2])  # Output: ['Black', 'Green']
print(tea_varieties[2:])  # Output: ['Oolong', 'White']
print(tea_varieties[2:2]) # Output: []

# Modifying list elements
tea_varieties[3] = "Herbal"
print(tea_varieties)  # Output: ['Black', 'Green', 'Oolong', 'Herbal']
print(tea_varieties[1:2]) # Output: ['Green']
tea_varieties[1:2] = "Lemon"
# SyntaxError: unmatched ')'
tea_varieties  # Output: ['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']

# Resetting the list
tea_varieties = ["Black", "Green", "Oolong", "White"]
print(tea_varieties[1:2])  # Output: ['Green']
tea_varieties[1:2] = ["Lemon"]
print(tea_varieties) # Output: ['Black', 'Lemon', 'Oolong', 'White']
print(tea_varieties[1:3])  # Output: ['Lemon', 'Oolong']
tea_varieties[1:3] = ["Green", "Masala"]
print(tea_varieties)  # Output: ['Black', 'Green', 'Masala', 'White']
print(tea_varieties[2:2]) # Output: []

# Inserting elements
tea_varieties[1:1] = ["test", "test"]
print(tea_varieties)  # Output: ['Black', 'test', 'test', 'Green', 'Oolong', 'White']
print(tea_varieties[1:2])  # Output: ['test']
print(tea_varieties[1:3]) # Output: ['test', 'test']

# Deleting elements
tea_varieties[1:3] = []  # deletion operation
print(tea_varieties)  # Output: ['Black', 'Green', 'Oolong', 'White']

# Replacing elements
tea_varieties[3] = ["Masala"]
print(tea_varieties) # Output: ['Black', 'Green', 'Oolong', ['Masala']]
tea_varieties[3] = "Masala"
print(tea_varieties) # Output: ['Black', 'Green', 'Oolong', 'Masala']

tea_varieties = ["Black", "Green", "Oolong", "White"]
tea_varieties[2] = "Masala"
print(tea_varieties) # Output: ['Black', 'Green', 'Masala', 'White']

# Iterating over a list
for tea in tea_varieties:
   print(tea)
# Output:
# Black
# Green
# Masala
# White

for tea in tea_varieties:
   print(tea, end="-")
# Output: Black-Green-Masala-White-

print(tea_varieties) # Output: ['Black', 'Green', 'Masala', 'White']

# Checking if an element exists in a list
if "Oolong" in tea_varieties:
   print("I have Oolong Tea")

# Adding an element to the end of the list
tea_varieties.append("Oolong")
print(tea_varieties)  # Output: ['Black', 'Green', 'Masala', 'White', 'Oolong']

if "Oolong" in tea_varieties:
   print("I have Oolong Tea") # Output: I have Oolong Tea

# Removing an element from the end of the list
print(tea_varieties.pop())  # Output: Oolong
print(tea_varieties)  # Output: ['Black', 'Green', 'Masala', 'White']

# Removing a specific element from the list
tea_varieties.remove("green")  # ValueError: list.remove(x): x not in list
# tea_varieties.remove(Green") # SyntaxError: unterminated string literal
tea_varieties.remove("Green")
print(tea_varieties) # Output: ['Black', 'Masala', 'White']

# Inserting an element at a specific index
tea_varieties.insert(1, "green")
print(tea_varieties) # Output: ['Black', 'green', 'Masala', 'White']

# Creating a copy of the list
tea_varieties_copy = tea_varieties.copy()
print(tea_varieties_copy)  # Output: ['Black', 'green', 'Masala', 'White']

# Appending an element to the copied list
tea_varieties_copy.append("Lemon")
print(tea_varieties)  # Output: ['Black', 'green', 'Masala', 'White']
print(tea_varieties_copy) # Output: ['Black', 'green', 'Masala', 'White', 'Lemon']

# List comprehension
squared_nums = [x**2 for x in range(10)]
print(squared_nums) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

y = range(10)
# cube_nums = [y**3 for x in rage(10)] # NameError: name 'rage' is not defined
cube_nums = [y**3 for x in range(10)]  # TypeError: unsupported operand type(s) for ** or pow(): 'range' and 'int'

squared_nums = [x**2 for x in range(10)]
# cube_nums = [y**3 for y in rage(10)] # NameError: name 'rage' is not defined
cube_nums = [y**3 for y in range(10)]
print(cube_nums) # Output: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]