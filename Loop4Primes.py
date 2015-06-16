
'''
Ziairi
COP 2271C-01 Introduction to Computation and Programming
Lab - Loop 4 - Display all prime numbers less than the input.
Last successful debugging: 6/16/15 4:36 PM
'''

# List of declared variables
UserInput = 0
State = 0
Prime = 0
Output = ""


# Recieve user input
UserInput = eval(input("Input a whole positive integer: "))

# Print first line of output
print("Here are the prime numbers that are less than your input:")


# Loop to find all prime numbers less than the input
for i in range(1, UserInput):
    
    # This loop ensures that all numbers are checked.
    for Count in range(2, i):
        
        # If State has no remainder, then it is not prime
        State = i % Count
        
        if State == 0:
            Prime =+ 1
            break;
    # If the variable of Prime is still 0, the number is prime
    if Prime == 0:
        print(i, end=" ")
        
    # Resets the Prime variable
    Prime = 0
    
print("")
print("Program is complete.")
print("^.^.^.^.^.^.^.^.^.^.^.^.^.^.^")
