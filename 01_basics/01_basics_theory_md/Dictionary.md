
## Python Dictionaries

Dictionaries in Python are unordered collections of key-value pairs. Each key in a dictionary must be unique, and it is used to access the corresponding value.

### Creating a Dictionary

You can create a dictionary using curly braces `{}` and separating each key-value pair with a colon `:`.

```python
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
```

### Accessing Values

You can access the value associated with a key using square brackets `[]` or the `get()` method.

```python
print(chai_types["Masala"])  # Output: 'Spicy'
print(chai_types.get("Ginger"))  # Output: 'Zesty'
```

If the key doesn't exist, using square brackets will raise a `KeyError`, while `get()` will return `None`.

```python
print(chai_types.get("Gingery"))  # Output: None
# chai_types["Gingery"]  # KeyError
```

### Modifying Values

You can change the value associated with a key by assigning a new value to that key.

```python
chai_types["Green"] = "Fresh"
```

You can also add a new key-value pair to the dictionary.

```python
chai_types["Earl Grey"] = "Citrus"
```

### Removing Items

You can remove a key-value pair from a dictionary using the `pop()` method or the `del` keyword.

```python
print(chai_types.pop("Ginger"))  # Output: 'Zesty'
del chai_types["Green"]
```

The `popitem()` method removes and returns an arbitrary key-value pair as a tuple.

```python
print(chai_types.popitem())  # Output: ('Earl Grey', 'Citrus')
```

### Iteration

You can iterate over the keys in a dictionary using a `for` loop.

```python
for chai in chai_types:
    print(chai)
```

To access both keys and values, you can use the `items()` method, which returns a view object containing the key-value pairs as tuples.

```python
for key, value in chai_types.items():
    print(key, value)
```

### Copying Dictionaries

You can create a shallow copy of a dictionary using the `copy()` method.

```python
chai_types_copy = chai_types.copy()
```

### Nested Dictionaries

Dictionaries can contain other dictionaries as values, creating nested structures.

```python
tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea": {"Green": "Fresh", "Black": "Strong"}
}
```

You can access values in nested dictionaries using multiple index operations.

```python
print(tea_shop["chai"])  # {'Masala': 'Spicy', 'Ginger': 'Zesty'}
print(tea_shop["chai"]["Ginger"])  # 'Zesty'
```

### Dictionary Comprehension

You can create a dictionary using a dictionary comprehension, which is a concise way to create a new dictionary from an existing iterable.

```python
squared_num = {x: x**2 for x in range(6)}
```

### Clearing a Dictionary

You can remove all key-value pairs from a dictionary using the `clear()` method.

```python
squared_num.clear()
print(squared_num)  # {}
```

### Creating Dictionaries from Keys

You can create a new dictionary from a sequence of keys using the `fromkeys()` method of the `dict` class. You can also specify a default value for all keys.

```python
keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
```

If you pass an iterable as the default value, it will be shared among all keys in the new dictionary.

```python
new_dict = dict.fromkeys(keys, keys)
print(new_dict)  # {'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
```