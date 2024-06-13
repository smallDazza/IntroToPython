
# def Greet():
#     print("I love coding")

# Greet()

# x = "outside"

# def test_score():
#     print(x)

# test_score()

# def test_score1():
#     scope = "inside"
#     print(scope)

# test_score1()


# def sum():
#     addition = 3 + 5
#     return addition

# result = sum()
# print(result)

# def colour():
#     a = 88
#     print("red")
#     print("Blue")
#     return a
#     print("white")
#     print("yellow")
    

# outcome = colour()
# print(outcome)

# def hello(n,l):
#     print(f"hello coder {n} {l}")


# hello("Mike","waters")

def even(num):
    return num % 2 ==0

def addNum():
    return int(input("Enter your number: "))

def Main():
    print("odd or even checker.")
    number = addNum()
    if even(number):
        print(f"{number} is a even number")
    else:
        print(f"{number} is a odd number")

Main()