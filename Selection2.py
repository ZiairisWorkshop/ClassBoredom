'''
Selection 2 Lab
'''
Degree = 0
UserInput = "Invalid"

# Makes sure that the user is using valid numbers for the input.
while UserInput == "Invalid":
    Degree = eval(input("Input a number between 0 and 360 for the direction: "))
            
    if (Degree < 0) or (Degree > 360):
        print("This is not a valid input")
        
    else:
        print("This is a valid input.")
        UserInput = "Valid"

# Calculates the direction on the compass

if (Degree > 348.75 and Degree <= 360) or (Degree >= 0 and Degree <= 11.25):
    print("This direction is East.")
    
elif Degree > 11.25 and Degree <= 33.75:
    print("This direction is North East East.")
    
elif Degree > 33.75 and Degree <= 56.25:
    print("This direction is North East.")
    
elif Degree > 56.25 and Degree <= 78.75:
    print("This direction is North North East.")

elif Degree > 78.75 and Degree <= 101.25:
    print("This direction is North.")

elif Degree > 101.25 and Degree <= 123.75:
    print("This direction is North North West.")

elif Degree > 123.75 and Degree <= 146.25:
    print("This direction is North West.")

elif Degree > 146.25 and Degree <= 168.75:
    print("This direction is North West West.")

elif Degree > 168.75 and Degree <= 191.25:
    print("This direction is West.")

elif Degree > 191.25 and Degree <= 213.75:
    print("This direction is South West West.")

elif Degree > 213.75 and Degree <= 236.25:
    print("This direction is South West.")

elif Degree > 236.25 and Degree <= 258.75:
    print("This direction is South South West.")

elif Degree > 258.75 and Degree <= 281.25:
    print("This direction is South.")

elif Degree > 281.25 and Degree <= 303.75:
    print("This direction is South South East.")

elif Degree > 303.75 and Degree <= 326.25:
    print("This direction is South East.")

elif Degree > 326.25 and Degree <= 348.75:
    print("This direction is South East East.")

    # The User should never see this line...
else:
    print("You are completely lost. Perhaps you should be looking up a survival guide instead...")

