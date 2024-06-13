
## Dictionaries = a collection of key-value pairs. Use the curly braces {}.
# are mutable = changes allowed.
# each key value is unique and the keys are used to store and retrieve the values
# stored using 'key':'value'
my_dict = {
    "Name" : "darren",
    "age" : "50",
    "city" : "sydney"
}

#access
print(my_dict["city"])
#adding a new item
my_dict["email"] = "dazza@gmail.com"
print(my_dict)

# adding to existing key
my_dict["city"] = "perth"
print(my_dict)

# remove a key-value pair
del my_dict ["age"]
print(my_dict)

my_dict.pop("email")
print(my_dict)

# check a specific key exists
print("email" in my_dict)
#........................
print(my_dict.keys())
print(my_dict.values())

#convert to list()

# list_of_keys = list(my_dict.keys())
# print(list_of_keys)

# iterate through a dictionary

for key, value in my_dict.items():
    print(f"{key} : {value}")

# nested dictionaries

nested_dict = {
    "person1" : {"name" : "alice", "age" : 34},
    "person2" : {"name" : "bob", "age" : 22}
}
print(nested_dict["person2"]["name"])

# merge dictionaries together - duplicate values will be appended
merge_dict = my_dict | nested_dict
print(merge_dict)