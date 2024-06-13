# Sets are defined by using curly braces {}

# my_set = {1,2,3,4, "apple"}
# print(my_set)

# my_set.add(5)
# print(my_set)
# my_set.remove(2)
# print(my_set)


# print(3 in my_set)

# Set operations = union (joins together(duplicates are removed)) , intersection (commonality or common value in all sets)
# difference (removes the common value in both sets from one set ) 
set_a = {1,2,3,7,8}
set_b = {4,5,6,7,8}
set_c = {7,8,9}

#Union
union_value = set_a.union(set_b)
print(union_value)

intersection = set_c.intersection(set_a)
print(intersection)

difference = set_b.difference(set_c)
print(difference)

