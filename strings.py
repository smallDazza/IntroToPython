#Variables = conventions
# snake_case    for python variables
# camelCase     for JavaScript
# PascalCase    for classes in all the languages
# kebab-case

# num1 = 7
# num2 = 10
# print(num1 + num2)

# = is assignment
# == is comparison

# num1 = num2
# print(num1 + num2)
# num3 = 5
# #string interpolation
# total = num2 + num1 + num3
# print("total of this =", total)  #uses a comma (cannot use +)
# print(f"total of this = {total}") # this is best convention to use

#Inputs
# length = input("Enter the length you need:")
# print(length)
# then a calculation will = error
# area = length * length
# print(area)  #because = string.

length = int(input("Enter the length you need:"))
print(length)
area = length * length
print(area)

#email example

first_name = input("Please enter your first name:")
last_name = input("Please enter your last name:")
company_name = input("Please enter your company name:")

print(f"{first_name}.{last_name}@{company_name}.com.au".lower())
#or
email = f"{first_name}.{last_name}@{company_name}.com.au".lower()
print(email)