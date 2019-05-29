def too_long(s):
    if len(s) >= 140:
        return True
    else:
        return False

#test a short string
print("this should be false:")
print(too_long("I'm a short string!"))

#test a long string
print("This should be true:")
print(too_long("Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal."))
