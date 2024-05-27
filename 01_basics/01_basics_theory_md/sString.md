# Working with Strings in Python

In Python, strings are sequences of characters enclosed within single quotes `'` or double quotes `"`.

## 1. String Slicing

Strings are immutable, but you can access their individual characters or substrings using indexing and slicing.

```python
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num_list[:])  # Output: '0123456789'
print(num_list[0:])  # Output: '0123456789'
print(num_list[:7])  # Output: '0123456'
print(num_list[0:7:2])  # Output: '0246'
print(num_list[0:7:3])  # Output: '036'
print(num_list[0:7:-1])  # Output: ''
print(num_list[0:-1])  # Output: '012345678'
```

The syntax for slicing is `string[start:stop:step]`:
- `start` is the index from where the slicing starts (inclusive)
- `stop` is the index where the slicing stops (not inclusive)
- `step` is the step size (optional, default is 1)

## 2. String Methods

Python provides various built-in methods to manipulate strings.

```python
chai = 'Masala Chai'
print(chai.lower())  # Output: 'masala chai'
print(chai.upper())  # Output: 'MASALA CHAI'

chai = '   Masala Chai   '
print(chai.strip())  # Output: 'Masala Chai'

chai = "lemon chai"
print(chai.replace("lemon", "Masala"))  # Output: 'Masala chai'
```

Some commonly used string methods are `lower()`, `upper()`, `strip()`, and `replace()`.

## 3. String Splitting and Joining

You can split a string into a list of substrings and join a list of substrings into a single string.

```python
chai = "lemon,Ginger,Masala,Mint"
print(chai.split(", "))  # Output: ['lemon,Ginger,Masala,Mint']

chai_variety = ["lemon", "Masala", "Ginger"]
print("".join(chai_variety))  # Output: 'lemonMasalaGinger'
chai = " ".join(chai_variety)  # Output: 'lemon Masala Ginger'
chai = ", ".join(chai_variety)  # Output: 'lemon, Masala, Ginger'
chai = "-".join(chai_variety)  # Output: 'lemon-Masala-Ginger'
```

The `split()` method splits a string into a list of substrings based on the specified separator. The `join()` method joins a list of strings into a single string with the specified separator.

## 4. String Indexing and Iteration

You can access individual characters in a string using indexing, and iterate over a string to process each character.

```python
chai = "Masala Chai"
print(len(chai))  # Output: 11
print(chai)  # Output: 'Masala Chai'

for letter in chai:
    print(letter)
# Output:
# M
# a
# s
# a
# l
# a
#
# C
# h
# a
# i
```

## 5. Escape Sequences

Escape sequences are used to represent special characters or control codes in strings.

```python
chai = "He said,\"Masala chai is awesome\""
print(chai)  # Output: 'He said,"Masala chai is awesome"'

chai = "Masala\nchai"
print(chai)
# Output:
# Masala
# chai

chai = r"Masala\nChai"
print(chai)  # Output: Masala\nChai

chai = r"c:\user\pwd"
print(chai)  # Output: c:\user\pwd
```

The backslash `\` is used as an escape character, and `\n` represents a newline character. The `r` prefix before a string creates a raw string literal, which treats backslashes as literal characters.

## 6. String Formatting

Python provides different ways to format strings, including the `format()` method and f-strings (Python 3.6+).

```python
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity, chai_type))  # Output: 'I ordered 2 cups of Masala chai'
```

The `format()` method allows you to substitute values into placeholders `{}` in a string.

## 7. String Operations

You can perform various operations on strings, such as checking for substrings, counting occurrences, and finding indices.

```python
chai = "Masala Chai"
print("Masala" in chai)  # Output: True
print("Masalaa" in chai)  # Output: False

chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))  # Output: 3
print(chai.find("Chai"))  # Output: 7
print(chai.find("chai"))  # Output: -1
```

The `in` operator checks if a substring is present in a string, `count()` returns the number of occurrences of a substring, and `find()` returns the index of the first occurrence of a substring (or -1 if not found).

These notes cover various aspects of working with strings in Python, including slicing, string methods, splitting and joining, indexing and iteration, escape sequences, string formatting, and common string operations.