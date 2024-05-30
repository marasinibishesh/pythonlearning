#Problem: Choose a mode of transportation based on the distance 
#(e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).
actualDistance=int(input("Enter the Distance in km: "))
mode=["Walk","Bike","Car"]
if(actualDistance<3):
    print("Mode of Transportation:",mode[0])
elif(actualDistance<=15):
    print("Mode of Transportation:",mode[1])
else:
    print("Mode of Transportation:",mode[2])