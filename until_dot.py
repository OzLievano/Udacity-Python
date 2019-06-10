#Write a function called until_dot that takes a string argument and return the portion of that dtring before the dot character.
def until_dot(s):
#Before the loop, create a variable to keep track of the current index.
    index = 0
#The while statement will need to check if the current index position is less than the length of the string.
    while index < len(s) and s[index] != '.':
#It will also need to check to make sure that the character of the current position is NOT a dot.
#Finally the function should return a slice, from the start of the string up to the index position of the fist dot.
        index += 1
    return(s[:index])



print(until_dot("Udacity.com"))

print(until_dot("you momma a hoe. Yo daddy is small."))
