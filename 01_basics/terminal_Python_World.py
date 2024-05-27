# 1. Print Statement
print("hello")  # Output: hello

# 2. Basic Arithmetic Operations
print(2 * 2)    # Output: 4
print(3 + 5)    # Output: 8

# 3. String Multiplication
print("chai" * 4)  # Output: 'chaichaichaichai'

# 4. Variable Assignment
score = 100
print(score)    # Output: 100
print(score)    # Output: 100

# 5. Undefined Variable
tea  # Raises NameError: name 'tea' is not defined

# 6. Invalid Non-Printable Character
print("^D")  # Raises SyntaxError: invalid non-printable character U+0004

# 7. Import os Module
import os

# 8. Get Current Working Directory
print(os.getcwd())  # Output: 'C:\\Users\\Laptop\\Documents\\pythonlearning'

# 9. Iterate Over a String
for c in "chai":
    print(c)
# Output:
# c
# h
# a
# i

# 10. Import sys Module
import sys

# 11. Get Platform Information
print(sys.platform)  # Output: 'win32'

# 12. Attempt to Use Undefined Function
ls  # Raises NameError: name 'ls' is not defined. Did you mean: 'os'?

# 13. Attempt to Import Non-existent Module
import hello_world  # Raises ModuleNotFoundError: No module named 'hello_world'

