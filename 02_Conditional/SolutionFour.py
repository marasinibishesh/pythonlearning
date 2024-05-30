#Problem: Determine if a fruit is ripe, overripe, 
#or unripe based on its color. 
#(e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
colorofBanana=input("Enter the color of Banana: ")
Banana={
    "Unripe":"Green","Ripe":"Yellow","Overripe":"Brown"
}
if colorofBanana==Banana["Unripe"]:
    print("Banana is Unripe")
elif colorofBanana==Banana["Ripe"]:
    print("Banana is ripe")
elif colorofBanana==Banana["Overripe"]:
    print("Banana is Overripe")
else:
    print("Can't Determine Sorry")