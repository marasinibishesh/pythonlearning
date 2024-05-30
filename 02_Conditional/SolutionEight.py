#Problem: Check if a password is "Weak", "Medium", or "Strong".
# Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
# counter:int=1
# for count, counter in zip(password, range(1,len(password)+1)):
#     print(count, counter)
'''password=input("Enter your password :")
counter:int=0
for count in password:
    counter+=1

if counter<6:
    print("Weak Password")
elif counter<=10:
    print("Medium Password")
else:
    print("Strong Pasword")'''
password=input("Enter your password :")
if len(password)<6:
    print("Weak Password")
elif len(password)<=10:
    print("Medium Password")
else:
    print("Strong Pasword")


