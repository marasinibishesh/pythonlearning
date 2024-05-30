#Problem: Customize a coffee order: "Small", "Medium", or "Large" 
#with an option for "Extra shot" of espresso.
sizeOption=["SMALL", "MEDIUM","LARGE"]
#Ask the user for the size of the coffee
coffeeSize=input("What size of coffee do you want? \n").upper()

if coffeeSize in sizeOption:
        shot=input("Do you need Extra shot of espresso ").upper()
        for coffee in sizeOption:
         if coffeeSize==coffee:
          if shot=="YES":
                print(f"Your order is {coffee.lower()} coffee with Extra shot of espresso ")
          else:
                print(f"Your order is {coffee.lower()} coffee ")

if coffeeSize not in sizeOption:
    print("Invalid Input")



