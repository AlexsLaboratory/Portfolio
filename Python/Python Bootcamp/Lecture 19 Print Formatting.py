"""
This will place the "s" variable into the print statement. The "%s" converts the "s" variable into a string to then be joined with the rest of the string.
"""
x = "String"
print("Place my variable here: %s" %(x))
# Output: Place my variable here: String


"""
This will cut off the "5" from the string since we specified how many spaces to show after the decimal point using this "%0.2f".
"""
print("Floating point number: %0.2f" %(13.145))
# Output: Floating point number: 13.14


"""
You can also insert more than one variable into a string.
"""
print("First: %s, Second: %s, Third: %s" %("one", "two", 3))
# Output: First: one, Second: two, Third: 3


"""
The more "Pythonic" way of doing the statement from above would be.

The reason for doing this is that you only have to define two variables (in this case) as long as you know the variable names you can use them anywhere in the string.
"""
print("First: {a}, Second: {b}, Third: {a}".format(a = "inserted", b = "one"))
# Output: First: inserted, Second: one, Third: inserted