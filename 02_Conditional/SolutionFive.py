#Problem: Suggest an activity based on the weather 
#(e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).
todayWeather=input("Enter today's weather condition: ")
activitySuggestion={"SUNNY":"Go for a walk","RAINY":"Read a book","SNOWY":"Build a snowman"}
if todayWeather.upper() in activitySuggestion:
    print(activitySuggestion[todayWeather.upper()])
else:
    print("Invalid input")
