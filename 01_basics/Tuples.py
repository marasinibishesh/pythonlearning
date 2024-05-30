# Creating a tuple
tea_types = ("Black", "Green", "Oolong")
print(tea_types)  # ('Black', 'Green', 'Oolong')

# Accessing elements
print(tea_types[0])  # 'Black'
print(tea_types[-1])  # 'Oolong'
print(tea_types[1:])  # ('Green', 'Oolong')

# Trying to modify an element (not allowed in tuples)
# tea_types[0] = "Lemon"  # TypeError: 'tuple' object does not support item assignment

# Length of a tuple
print(len(tea_types))  # 3

# Concatenating tuples
more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
print(all_tea)  # ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')

# Membership test
if "Green" in all_tea:
    print("I have Green Tea")
# I have Green Tea

# Duplicates allowed in tuples
more_tea = ("Herbal", "Earl Grey", "Herbal")
print(more_tea.count("Herbal"))  # 2
print(more_tea.count("Herb"))  # 0

# Original tuple remains unchanged
print(tea_types)  # ('Black', 'Green', 'Oolong')

# Unpacking a tuple
black, green, Oolong = tea_types
print(black)  # 'Black'

# Checking the type
print(type(tea_types))  # <class 'tuple'>

# Nesting is allowed in tuples