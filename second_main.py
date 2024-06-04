#Variables = conventions
# snake_case    for python variables
# camelCase     for JavaScript
# PascalCase    for classes in all the languages
# kebab-case

num1 = 7
num2 = 10
print(num1 + num2)

# = is assignment
# == is comparison

num1 = num2
print(num1 + num2)
num3 = 5
#string interpolation
total = num2 + num1 + num3
print("total of this =", total)  #uses a comma (cannot use +)
print(f"total of this = {total}") # this is best convention to use