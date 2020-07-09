# python 3.8
# Author: Christian Morra
# creates an empty dictionary
d = {}
# creates a new boolean validKey and sets it to False
validKey = False
# This loop makes it so it keeps asking the user for a key. Since it's while True it won't stop until a break command is executed
while True:
    # asks the user for input and sets that to keyInput
    keyInput = input("Enter a key, or type 'done' to finish: ")

    # first if/elif/else block

    # if what they typed was a key contained in the dictionary d, then set validKey to False
    if keyInput in d:
        validKey = False
    # if they type 'done' then break the loop, which will bring us to 'print("Bye bye."), since it skips everything else in the loop
    elif keyInput == 'done':
        break
    # otherwise (meaning the key is not yet in the dictionary, and they don't want to exit, set validKey to True
    else:
        validKey = True

    # end of the first if/elif/else block

    # second if block
    # validKey is False if what they typed was already inside the dictionary
    if validKey == False:
        # ask the user if they want to overwrite the value that's currently at  d[keyInput]
        yesNo = input(f"That key already exists in this dictionary with a value of {d[keyInput]}, overwrite? (y/n): ")
        # nested if statement block
        # if they say 'y', set validKey to True, which later lets them provide a value
        if yesNo == 'y':
            validKey = True
        # otherwise set it to (or keep it at) False. This line is technically unencessary because if we don't change validKey to True, it's already at False because the if statement before this checked if it was False already
        else:
            validKey = False

    # third if block
    # validKey is true if the key didn't exist in the dictionary, or if the user said they wanted to overwrite an existing key
    if validKey == True:
        # Ask for a value and assign it to d[keyInput]. If keyInput already existed in d, it is overwritten, otherwise it is added to the dictionary
        valueInput = input("Enter a value: ")
        d[keyInput] = valueInput
    print(f'The current dictionary is {d}')
    # loop back to the beginning of the loop
print("Bye bye.")