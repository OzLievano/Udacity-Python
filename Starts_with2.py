# Add your function definition here
def starts_with(s1,s2):
    if s1[0] == s2[0]:
        return True
    else:
        return False


# A call like this should return True:
print(starts_with("banana", "bread"))

# And one like this should return False:
print(starts_with("zebonkey", "kiwi"))
