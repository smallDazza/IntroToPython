
def pers_details(**kwargs):
    for key, value in kwargs.items():
        print (f" {key} ---> {value}")


pers_details(name = "dazza", age = "45", height = "185")

#using both args & kwargs =

def myFunction(*onestar, **twostars):
    print("args: ", onestar)
    print("kwargs: ", twostars)

myFunction('I', 'Love', 'Coding', 5,6,7, first = "I", second = "love", third = "Coding!!!")
