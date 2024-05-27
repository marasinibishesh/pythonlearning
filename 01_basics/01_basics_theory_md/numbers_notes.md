
1. **Basic Arithmetic Operations**
   - Addition: `x + y`
   - Subtraction: `x - y`
   - Multiplication: `x * y`
   - Division: `x / y` (returns a floating-point value)
   - Integer Division: `x // y` (returns the quotient as an integer, discarding the remainder)
   - Modulus: `x % y` (returns the remainder after division)
   - Exponentiation: `x ** y` (x raised to the power of y)

```python
x = 2
y = 3
z = 4

print(x + y)     # Output: 5
print(x + y * z) # Output: 14
print((x + y) * z) # Output: 20
print(x + (y * z)) # Output: 14
```

2. **Data Types**
   - `int`: Represents integer values
   - `float`: Represents floating-point values
   - `complex`: Represents complex numbers

```python
print(int(2.23))   # Output: 2
print(float(40))   # Output: 40.0
print(2 + 1j * 3)  # Output: (2+3j)
```

3. **Numeric Representations**
   - Decimal: `42`
   - Octal: `0o20` (equivalent to 16 in decimal)
   - Hexadecimal: `0xff` (equivalent to 255 in decimal)
   - Converting between bases: `int(value, base)`

```python
print(oct(64))     # Output: '0o100'
print(hex(64))     # Output: '0x40'
print(int('64', 8))  # Output: 52 (converting from octal)
print(int('64', 16)) # Output: 100 (converting from hexadecimal)
```

4. **Bitwise Operations**
   - Left Shift: `x << n` (shifts the bits of x to the left by n places)
   - Right Shift: `x >> n` (shifts the bits of x to the right by n places)

```python
x = 1
print(x << 2)      # Output: 4 (equivalent to 1 * 2^2)
```

5. **Random Numbers**
   - `random.random()`: Generates a random floating-point number between 0 and 1
   - `random.randint(a, b)`: Generates a random integer between a and b (inclusive)
   - `random.choice(sequence)`: Randomly selects an element from a sequence
   - `random.shuffle(sequence)`: Shuffles the elements of a sequence in-place

```python
import random

print(random.random())           # Output: A random float between 0 and 1
print(random.randint(1, 10))     # Output: A random integer between 1 and 10
my_list = ['lemon', 'masala', 'ginger', 'mint']
print(random.choice(my_list))    # Output: A random element from the list
random.shuffle(my_list)
print(my_list)                   # Output: The shuffled list
```

6. **Decimal and Fractional Arithmetic**
   - The `decimal` module provides support for accurately representing decimal numbers
   - The `fractions` module provides support for working with fractions

```python
from decimal import Decimal
from fractions import Fraction

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))  # Output: Decimal('0.0')
my_fraction = Fraction(2, 7)
print(my_fraction)               # Output: Fraction(2, 7)
```

7. **Set Operations**
   - Union: `set1 | set2`
   - Intersection: `set1 & set2`
   - Difference: `set1 - set2`

```python
set_one = {1, 2, 3, 4}
print(set_one & {1, 3})          # Output: {1, 3}
print(set_one | {1, 3})          # Output: {1, 2, 3, 4}
print(set_one - {1, 2, 3, 4})    # Output: set()
```

8. **Type Checking**
   - `type(value)`: Returns the type of the given value
   - `isinstance(value, type)`: Checks if the value is an instance of the specified type

```python
print(type({}))     # Output: <class 'dict'>
print(type(True))   # Output: <class 'bool'>
print(True == 1)    # Output: True
print(False == 0)   # Output: True
```

With these notes and code examples, you can practice working with numbers in Python, covering various operations, data types, and related modules.