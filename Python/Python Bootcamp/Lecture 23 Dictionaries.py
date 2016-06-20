"""
Example of a basic dictionary.
"""
my_dictionary = {"k1":"value1", "k2":"value2"}
print(my_dictionary["k1"])
# Output: value1


"""
You can have a dictionary with different types of elements in it
such as strings, integers, and floating point numbers.
"""
my_dictionary1 = {"k1":123, "k2":3.5, "k3":"string"}
print(my_dictionary1["k2"])
# Output: 3.5


"""
You can index this string and you can call different methods on it such as ".upper()".
"""
my_dictionary2 = {"k1":123, "k2":3.5, "k3":"string"}
print(my_dictionary2["k3"][::-1].upper())
# Output: GNIRTS


"""
You can affect values in a dictionary.
"""
my_dictionary3 = {"k1":123, "k2":3.5, "k3":"string"}
print(my_dictionary3["k1"])
# Output: 123
my_dictionary3["k1"] = my_dictionary3["k1"] - 120
print(my_dictionary3["k1"])
# Output: 3

# Or

"""
A much faster way to do that same stuff above this.
"""
my_dictionary4 = {"k1":123, "k2":3.5, "k3":"string"}
print(my_dictionary4["k1"])
# Output: 123
my_dictionary4["k1"] -= 120
print(my_dictionary4["k1"])
# Output: 3


"""
You can add keys to a empty dictionary.
"""
empty_dictionary = {}
empty_dictionary["animal"] = "Dog"
empty_dictionary["answer"] = 64
print(empty_dictionary)
# Output: {'answer': 64, 'animal': 'Dog'}


"""
You can have nested dictionaries and you can index them and call different methods on them too.
"""
empty_dictionary1 = {"k1": {"nestkey": {"subnestkey": "value"}}}
print(empty_dictionary1["k1"]["nestkey"]["subnestkey"][::-1].upper())
# Output: EULAV


"""
Printing out specific parts of the dictionary.
"""
my_dictionary5 = {"k1":1, "k2":2, "k3":3}
print(my_dictionary5.keys())
# Output: dict_keys(['k2', 'k3', 'k1'])
print(my_dictionary5.values())
# Output: dict_values([2, 3, 1])
print(my_dictionary5.items())
# Output: dict_items([('k2', 2), ('k3', 3), ('k1', 1)])