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

# print(list(range(5, 0, -1)))
# print(list(range(0, 14, 2)))

# string_list = input("enter values for list(with spaces): ")

# list1 = string_list.split()
# print(list1)

n = int(input("enter a number for the size of a list: "))

list2 = list(map(int, input("enter the list numbers: ").strip().split()))[:n]

print(f"the list is: {list2}")


    

