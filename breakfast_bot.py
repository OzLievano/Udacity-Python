# 2-second delay in response. Will need to use time

# program must do this :
    # Get input and use it to determine what happens next
    # Handle bad input without crashing
    # Be flexible with the input the user can enter
    # print message to the console, with a short pause
    # Allow the player to order again if they like


# Input & Conditionals
# input function always returns a string ****
# int() & str() functions to change type

print("Hello! I am Bob, the Breakfast Bot.")
print("Today we have two breakfasts available.")
print("The first is waffles with strawberries and whipped cream.")
print("The second is sweet potato pancakes with butter and syrup")

while True:

    menu_choice = input(
    "Please place your order."
    "Would you like waffles or pancakes?\n").lower()

    if menu_choice == 'Waffles' in menu_choice:
        print('Waffles it is!')
        break
    elif menu_choice == 'Pancakes' in menu_choice:
        print('Pancakes it is!')
        break
    else:
        print("Sorry, I don't understand.")
print('Your order will be ready shortly')
# Getting Valid Input
