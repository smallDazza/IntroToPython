
# tuples are immutable = no changes can be done.
### Tuples are immuteable = no changes

my_tuple = (1,2, "A", "happy")

print(my_tuple[3])

# tuples can be unpacked:

a,b,c,d = my_tuple
print(a, d)

#nested tuple
nested_tuple = (1,2, (3,4), (5,6))
print(nested_tuple[2][1])