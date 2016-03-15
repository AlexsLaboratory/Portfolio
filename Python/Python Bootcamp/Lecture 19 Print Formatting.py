
"""
This will place the "s" variable into the print statement. The "%s" converts the "s" variable into a string to then be joined with the rest of the string.
"""
s = "String"
print("Place my variable here: %s" %(s))



"""
This will cut off the "5" from the string since we specified how many spaces to show after the decimal point using this "%0.2f".
"""
print("Floating point number: %0.2f" %(13.145))



"""
You can also insert more than one variable into a string.
"""
print("First: %s, Second: %s, Third: %s" %("one", "two", 3))



"""
The more "Pythonic" way of doing the statement from above would be.

The reason for doing this is that the order of the variables can be moved around as much as you want. You do not need to know the right order, instead now you just need to know the variables.
"""
print("First: {x}, Second: {y}, Third: {x}".format(x = "inserted", y = "one"))