# 1. Variable Assignment
x = 2
y = 3
z = 4

# 2. Basic Arithmetic Operations
print(x + y)     # Output: 5
print(x + y * z) # Output: 14
print((x + y) * z) # Output: 20
print(x + (y * z)) # Output: 14

# 3. Mixed Data Types in Arithmetic Operations
print(40 + 2.23) # Output: 42.23
print('bishesh' + 3) # TypeError: can only concatenate str (not "int") to str

# 4. Type Conversions
print(int(2.23)) # Output: 2
print(float(40)) # Output: 40.0
print('chai' + 'code') # Output: 'chaicode'

# 5. Tuple Unpacking
x, y, z = 2, 3, 4
print(x, y, z) # Output: (2, 3, 4)

# 6. Multiple Assignment
print(x + 1, y * 2) # Output: (3, 6)

# 7. Modulus Operator
print(y % 2) # Output: 1

# 8. Exponentiation
print(z ** 2) # Output: 16
print(100 ** 2) # Output: 10000
print(2 * 100) # Output: 200
print(2 ** 100) # Output: 1267650600228229401496703205376
print(2 * 1000) # Output: 2000
print(2 ** 1000) # Output: 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376

# 9. Division and Floating-Point Representation
result = 1 / 3.0
print(result) # Output: 0.3333333333333333

# 10. String Representation
print(repr('chai')) # Output: "'chai'"
print(str('chai'))  # Output: 'chai'
print('chai')       # Output: chai

# 11. Comparisons
print(1 < 2)  # Output: True
print(True)   # Output: True

# 12. Integer Division
print(22 // 7) # Output: 3
print(22 / 7)  # Output: 3.142857142857143

# 13. Floating-Point Comparisons
print(5.0 == 5.0) # Output: True
print(4.0 != 5.0) # Output: True

# 14. Chained Comparisons
print(x, y, z)     # Output: (2, 3, 4)
print(x < y < z)   # Output: True
print(x < y and y < z) # Output: True

# 15. Boolean Expressions
print(1 == 2 < 3)  # Output: False
print(1 == 2 and 2 < 3) # Output: False

# 16. Math Module
import math
print(math.floor(3.5))   # Output: 3
print(math.ceil(3.5))    # Output: 4
print(math.floor(-3.5))  # Output: -4
print(math.ceil(-3.5))   # Output: -3
print(math.trunc(2.8))   # Output: 2
print(math.trunc(-2.8))  # Output: -2

# 17. Large Integer Arithmetic
print(9999999999999999999999999999999999999999 + 1) # Output: 10000000000000000000000000000000000000000

# 18. Complex Numbers
print(2 + 1j)      # Output: (2+1j)
print(2 + 1j * 3)  # Output: (2+3j)
print((2 + 1j) * 3) # Output: (6+3j)

# 19. Octal and Hexadecimal Representations
print(0o20)   # Output: 16
print(0xff)   # Output: 255
print(oct(64))# Output: '0o100'
print(hex(64))# Output: '0x40'

# 20. Base Conversions
print(int(3.14))   # Output: 3
print(int('64', 8))  # Output: 52
print(int('64', 16)) # Output: 100

# 21. Bitwise Operations
x = 1
print(x << 2)  # Output: 4

# 22. Random Module
import random
print(random.random())       # Output: A random float between 0 and 1
print(random.randint(1, 10)) # Output: A random integer between 1 and 10
l1 = ['lemon', 'masala', 'ginger', 'mint']
print(random.choice(l1))     # Output: A random element from the list
random.shuffle(l1)
print(l1)                    # Output: The shuffled list

# 23. Floating-Point Precision Issues
print(0.1 + 0.1 + 0.4)            # Output: 0.6000000000000001
print((0.1 + 0.1 + 0.1) - 0.3)    # Output: 5.551115123125783e-17

# 24. Decimal Module
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') + Decimal('0.3')) # Output: Decimal('0.6')
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')) # Output: Decimal('0.0')

# 25. Fractions Module
from fractions import Fraction
myFra = Fraction(2, 7)
print(myFra)  # Output: Fraction(2, 7)

# 26. Set Operations
setone = {1, 2, 3, 4}
print(setone & {1, 3})  # Output: {1, 3}
print(setone | {1, 3})  # Output: {1, 2, 3, 4}
print(setone - {1, 2, 3, 4}) # Output: set()

# 27. Type Checking
print(type({}))  # Output: <class 'dict'>
print(type(True))# Output: <class 'bool'>
print(True == 1) # Output: True
print(False == 0)# Output: True
print(True is 1) # Output: False (with SyntaxWarning)