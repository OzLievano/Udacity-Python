#when we have seperate lines of code
# python treats them as exactly that
# seperate lines of code

# explcit line-joining example

story = "Once upon a time there was a very logn string that \
over 100 characters long and could not all fit on the \
screen at once."

print(story)

# Implicit line-joining example
# Expressions inside (),[],{}
# can be split over more than one line

my_list = [1,2,3,4,5,6,7,9,10,11,12,13,14,
15,16,17,18,19,20,21,22,23,24,25,26,27,28
29,30,31,32,33,34,35,36,37,38,39,40,41,42]

# Python will essentially treat these three lines
# the same as if they were a single line


# Python concatenates any adjacent string
# KNown as Automatic string literal concatenation

"foo" "bar"
>>> 'foobar'
