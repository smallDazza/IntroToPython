
a = 10
# b = 15

# result = a + b

# print(f"the result of {a} plus {b} equals {result}")

# today = "tuesday"

# if today == "monday":
#     print("set an alarm for 5am")
# elif today == "tuesday":
#     print("set an alarm for 7am")
# elif today == "wednesday":
#     print("set alarm for 8am")

# temp = 36

# if temp > 35:
#     print("its hot outside")
# elif temp < 15:
#     print("its cold outside")
# else:
#     print("temp is just right")

# pass property
#does nothing , just passes..........(same as return in js)
# if temp > 35:
#     pass
# elif temp < 15:
#     print("its cold outside")
# else:
#     print("temp is just right")

# Boolean  Operators
# AND, OR, NOT Operands needs to be boolean as well

# a = True
# b = False
# result = a and b
# print(result)

# result = a or b
# print(result)

# result = not b
# print(result)

# age = 35
# has_permission = True

# if age >= 20:
#     if has_permission:
#         print("acces granted")
#     else:
#         print("access denied")
# else:
#     print("access denied")

# # but could do:
# if age >= 18 and has_permission:
#     print("access granted")
# else:
#     print("access denied")

## but:  Ternary Operater
# "result" if  (condition) else  "result"

# print("access granted") if age >= 18 and has_permission else print("acces denied")

# Match-case = control flow similar to switch statements in other languages

# day_number = 3

# match day_number:
#     case 1:
#         day_name = "monday"
#     case 2:
#         day_name = "tuesday"
#     case 3:
#         day_name = "wednesday"
#     case 4:
#         day_name = "thursday"

# print(day_name)

#activity

# grade = int(input("Enter your score: "))

# if grade > 100:
#     grade = "N/A"
# elif grade >= 90 and grade <= 100:
#     grade = "A"
# elif grade >= 80:
#     grade = "B"
# elif grade >= 70:
#     grade = "C"
# elif grade >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print(grade)

#practice activity

number1 = float(input("Enter first number: "))
operation = input(" Enter the operation (+,-,*,/): ")
number2 = float(input("Enter the second number: "))

if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        print("cannot divide")

print(f"the result = {result}")





