#Problem: Recommend a type of pet food based on the pet's species and age. 
#(e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
petAnimal={"DOG":"Puppy food","CAT":"Senior cat food"}
yourPet=input("Enter your pet's species :").upper()
yourpetAge=int(input("Enter your pet age :"))

if yourPet in petAnimal:
    if yourPet=="DOG":
      if yourpetAge<=2:
            print(f"Pet food of {yourPet.lower()} of age {yourpetAge} is {petAnimal['DOG']}")
      else:
          print("We don't have pet food for dog above 2 years Sorry")
         
    else:
        if yourpetAge>=5:
            print(f"Pet food of {yourPet.lower()} of age {yourpetAge} is {petAnimal['CAT']}")
        else:
          print("We don't have pet food for cat bellow 5 years Sorry")


