#Write your function definition here

def starts_K(string):
    if string[0] == 'K':
        return True
    else:
        return False

#A function call like this should return True:
print(starts_K("Kelly"))

#And one like this should returbn False:
print(starts_K("Abe"))
