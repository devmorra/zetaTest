choice = "right"
while(choice != "left"):
  choice = input("You're in a forest. Would you like to take the left or right path?")
  if(choice == 'left'):
    print("You took the left path, which led out of the forest")
  elif(choice == 'right'):
    print("You took the right path, which looped back to the original intersection")
  else:
    print("Sorry, please say left or right")
print("You make it out of the forest!")