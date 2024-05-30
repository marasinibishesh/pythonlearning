#Problem: Determine if a year is a leap year. (Leap years are 
#divisible by 4, but not by 100 unless also divisible by 400).
enteredYear=int(input("Enter a year :"))
if (enteredYear%400==0) or (enteredYear%4==0 and enteredYear%100!=0):
    print(f"{enteredYear} is a leap year.")
else:
    print(f"{enteredYear} isn't a leap year.")