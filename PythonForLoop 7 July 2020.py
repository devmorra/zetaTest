# =============================================================================
# Goal is to create a simple for-loop
# 
# Pseudo-code:
#     1.) Ask the user how many days has it been raining for
#     2.) Print each day using the for-loop for how many days from the user input
#     3.) Then ask how much each day it has been raining for
#     4.) Add each day together using a for-loop
# =============================================================================

userRainDays = int(input("How many days did it rain? "))
userSum = 0

for days in range(userRainDays):
    userRainMeas = input("Day: " + str(days + 1) + ": How many inches did it rain? " )
    userSum += int(userRainMeas)
    
print("\nOverall total inches of rain is: " + str(userSum))