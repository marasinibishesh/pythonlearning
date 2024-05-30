'''
if score >= 101:
    print("Please verify your grade again")
    exit()
'''
studentScore=int(input("Enter your score"))
if studentScore>100:
    print("Invalid Score")
else:
    if studentScore>=90:
        print("A")
    elif studentScore>=80:
        print("B")
    elif studentScore>=70:
        print("C")
    elif studentScore>=60:
        print("D")
    else:
        print("F")