# Add your code here.
def total_length(alist):
    x = 0
    for string in alist:
        x = x + len(string)
    return x 


# Should return 6:
print(total_length(['foo', 'bar']))

# Should return 0 (it's an empty list):
print(total_length([]))

# Should return 8:
