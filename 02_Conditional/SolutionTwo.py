todaysDay=input("Enter the day name:")
person_age=int(input("Enter your age:"))
price=int(12 if person_age>=18 else 8)

if todaysDay.upper()=="WEDNESDAY":
    print(f"Today is Wednesday! The discounted ticket price is ${price-2}")
else:
    print(f"The regular ticket price is ${price}")
    
 





  
