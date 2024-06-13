### Lists are mutable = can do changes
# Composite data type = multiple data types stored in one variable
# each called a element

# country1 = "australia"
# country2 = "england"
# country3 = "usa"
# country4 = "NZ"

# countries = ["aust","eng","usa","NZ"]

# print(countries)

# print(countries[2])

# countries[1] = "sth africa"
# print(countries)

# countries.append("NZ")
# print(countries)

# countries.remove("usa")
# print(countries)

# print("Total length of the list:", len(countries))

print(list(range(5, 0, -1)))
print(list(range(0, 14, 2)))

### Tuples are immuteable = no changes

my_tuple = (1,2, "A", "happy")

print(my_tuple[3])

# tuples can be unpacked:

a,b,c,d = my_tuple
print(a, d)

#nested tuple
nested_tuple = (1,2, (3,4), (5,6))
print(nested_tuple[2][1])


    

