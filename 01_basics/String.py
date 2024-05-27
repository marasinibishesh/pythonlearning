# Slicing Lists
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num_list[:])  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num_list[0:])  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num_list[:7])  # Output: [0, 1, 2, 3, 4, 5, 6]
print(num_list[0:7:2])  # Output: [0, 2, 4, 6]
print(num_list[0:7:3])  # Output: [0, 3, 6]
print(num_list[0:7:-1])  # Output: []
print(num_list[0:-1])  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# String Methods
chai = 'Masala Chai'
print(chai.lower())  # Output: masala chai
print(chai.upper())  # Output: MASALA CHAI
chai = "   Masala Chai   "
print(chai.strip())  # Output: Masala Chai
chai = "lemon chai"
print(chai.replace("lemon", "Masala"))  # Output: Masala chai
chai = "lemon,Ginger,Masala,Mint"
print(chai.split(", "))  # Output: ['lemon,Ginger,Masala,Mint']
chai = "Masala Chai"
print(chai.find("Chai"))  # Output: 7
print(chai.find("chai"))  # Output: -1
chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))  # Output: 3

# String Formatting
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity, chai_type))  # Output: I ordered 2 cups of Masala chai

# Converting List to String
chai_variety = ["lemon", "Masala", "Ginger"]
print("".join(chai_variety))  # Output: lemonMasalaGinger
chai = " ".join(chai_variety)  # Output: lemon Masala Ginger
chai = ",  ".join(chai_variety)  # Output: lemon,  Masala,  Ginger
chai = "- ".join(chai_variety)  # Output: lemon- Masala- Ginger

# String Length and Iteration
chai = "Masala Chai"
print(len(chai))  # Output: 11
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

# Escape Sequences
chai = "He said,\"Masala chai is awesome\""
print(chai)  # Output: He said,"Masala chai is awesome"
chai = "Masala\nchai"
print(chai)  # Output: Masala (newline) chai
chai = r"Masala\nChai"
print(chai)  # Output: Masala\nChai (raw string)
chai = r"c:\user\pwd"
print(chai)  # Output: c:\user\pwd

# String Membership Test
chai = "Masala Chai"
print("Masala" in chai)  # Output: True
print("Masalaa" in chai)  # Output: False