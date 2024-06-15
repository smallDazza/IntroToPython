
# Wilcard Arguments = when dont know how many arguments to pass in a function
# Non - keyword arguments =  *args
# Keyword arguments = **kwargs (dictionary parameters)

#using:
def add(*args):
    sum = 0
    for each in args:
        sum += each
    return sum

def subtract(*args):
    difference = args[0]
    for each in args[1:]:
        difference = difference - each
    return difference

def multiply(*args):
    multiply = 1
    for each in args:
        multiply *= each
    return multiply

def divide(a,b):
    if b == 0:
        return "Error! Division by Zero"
    return a / b


