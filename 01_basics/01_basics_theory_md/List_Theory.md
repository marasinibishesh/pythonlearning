# Lists in Python

Lists are ordered collections of items. They are mutable, meaning their elements can be modified after creation. Lists are defined using square brackets `[ ]` with comma-separated values.

## Accessing List Elements

```python
tea_varieties = ["Black", "Green", "Oolong", "White"]
print(tea_varieties[0])    # Output: Black
print(tea_varieties[-1])   # Output: White
print(tea_varieties[1:3])  # Output: ['Green', 'Oolong']
print(tea_varieties[:3])   # Output: ['Black', 'Green', 'Oolong']
print(tea_varieties[2:])   # Output: ['Oolong', 'White']
print(tea_varieties[2:2])  # Output: []
```

## Modifying Lists

```python
tea_varieties[3] = "Herbal"       # Replacing an element
print(tea_varieties)              # Output: ['Black', 'Green', 'Oolong', 'Herbal']

tea_varieties[1:2] = ["Lemon"]    # Replacing a sublist
print(tea_varieties)              # Output: ['Black', 'Lemon', 'Oolong', 'White']

tea_varieties[1:3] = ["Green", "Masala"]  # Replacing a sublist
print(tea_varieties)              # Output: ['Black', 'Green', 'Masala', 'White']

tea_varieties[1:1] = ["test", "test"]  # Inserting elements
print(tea_varieties)              # Output: ['Black', 'test', 'test', 'Green', 'Oolong', 'White']

tea_varieties[1:3] = []           # Deleting a sublist
print(tea_varieties)              # Output: ['Black', 'Green', 'Oolong', 'White']
```

## List Methods

```python
tea_varieties.append("Oolong")    # Adding an element to the end
print(tea_varieties)              # Output: ['Black', 'Green', 'Masala', 'White', 'Oolong']

print(tea_varieties.pop())        # Output: Oolong (removes and returns the last element)
print(tea_varieties)              # Output: ['Black', 'Green', 'Masala', 'White']

tea_varieties.remove("Green")     # Removing a specific element
print(tea_varieties)              # Output: ['Black', 'Masala', 'White']

tea_varieties.insert(1, "green")  # Inserting an element at a specific index
print(tea_varieties)              # Output: ['Black', 'green', 'Masala', 'White']

tea_varieties_copy = tea_varieties.copy()  # Creating a copy of the list
print(tea_varieties_copy)         # Output: ['Black', 'green', 'Masala', 'White']
```

## List Comprehension

List comprehension is a concise way to create lists from other iterables.

```python
squared_nums = [x**2 for x in range(10)]
print(squared_nums)               # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cube_nums = [y**3 for y in range(10)]
print(cube_nums)                  # Output: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```

This markdown file covers the basics of lists in Python, including accessing elements, modifying lists, list methods, and list comprehension, based on the examples provided in the given file.