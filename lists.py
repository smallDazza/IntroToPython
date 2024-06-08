
# Composite data type = multiple data types stored in one variable
# each called a element

country1 = "australia"
country2 = "england"
country3 = "usa"
country4 = "NZ"

countries = ["aust","eng","usa","NZ"]

print(countries)

print(countries[2])

countries[1] = "sth africa"
print(countries)

countries.append("NZ")
print(countries)

countries.remove("usa")
print(countries)

print("Total length of the list:", len(countries))
