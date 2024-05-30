## Python Tuples

Tuples in Python are ordered, immutable collections of items. They are defined using parentheses `()` or the `tuple()` constructor.

### Creating a Tuple

You can create a tuple by enclosing a comma-separated sequence of items within parentheses.

```python
tea_types = ("Black", "Green", "Oolong")
```

### Accessing Elements

You can access individual elements in a tuple using square bracket indexing, just like lists. Indexing starts from 0.

```python
print(tea_types[0])  # Output: 'Black'
print(tea_types[-1])  # Output: 'Oolong' (negative indexing for reverse order)
```

You can also use slicing to retrieve a subset of the tuple.

```python
print(tea_types[1:])  # Output: ('Green', 'Oolong')
```

### Immutability

Tuples are immutable, which means you cannot modify or reassign individual elements once the tuple is created.

```python
# tea_types[0] = "Lemon"  # TypeError: 'tuple' object does not support item assignment
```

### Length

You can find the length of a tuple using the `len()` function.

```python
print(len(tea_types))  # Output: 3
```

### Concatenation

You can concatenate two or more tuples using the `+` operator.

```python
more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
print(all_tea)  # Output: ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
```

### Membership Test

You can check if an element is present in a tuple using the `in` operator.

```python
if "Green" in all_tea:
    print("I have Green Tea")
# Output: I have Green Tea
```

### Counting Occurrences

You can count the number of occurrences of an element in a tuple using the `count()` method.

```python
more_tea = ("Herbal", "Earl Grey", "Herbal")
print(more_tea.count("Herbal"))  # Output: 2
print(more_tea.count("Herb"))  # Output: 0
```

### Unpacking

You can unpack the elements of a tuple into separate variables.

```python
black, green, Oolong = tea_types
print(black)  # Output: 'Black'
```

### Type Checking

You can check the type of an object using the `type()` function.

```python
print(type(tea_types))  # Output: <class 'tuple'>
```

### Nesting

Tuples can contain other tuples, allowing you to create nested data structures.

```python
# Nesting is allowed in tuples
```