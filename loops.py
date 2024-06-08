
# Used to repeat a block of code multiple times until a condition is met
# use DRY coding principles - Dont Repeat Yourself

# If condition would decide whether or not to run the intended block
# Loops would decide how many times the user wants to run the intended block

# while loop
# while the condition is met keep executing the intended block of code, if not met , skip the block.
# thins to consider: program can enter the loop, program can exit the loop

# no_coins = 4
# while no_coins > 0:
#     print("counted 1: ")
#     no_coins -= 1


# while users_guess != guess_num:
#     users_guess = int(input("whats your guess( 1 to 10): "))

# print("correct")

# guess_num = 5

# users_guess = None
# while users_guess != guess_num:
#     users_guess = int(input("whats your guess( 1 to 10): "))

#     if users_guess < guess_num:
#         print("to low")
#     elif users_guess> guess_num:
#         print("too high")
#     else:
#         print("correct")

## Range =its a predefined function that generates a sequence of numbers
#useful for iterating a specific number of time over a sequence of numbers.
# range(paramaters) = range(start, stop, step)
#eg range(1, 2, 3)
# print(range(5, 10, 1)) #a range of 5 because started at 5

### for loops
#for each time in a sequence , execute the intended blocks/statements

# for loop in a range
# for each in range(10,2,-2):
#     print (each)
# # for loop in a list
# fruits = ["apple","banana","orange"]
# for each in fruits:
#     print(each)

# for i in "dazza":
#     print(i)

# for i in range(len(fruits)):
#     print(f"index {i}: {fruits[i]}")


#activity
# initialise the variable
# total = 0
# # loop through the range and sum each number
# for each in range(11):
#     total += each
# # print the total
# print("the sum of the 10 numbers =", total)

# Loop Control statements
# control the flow of the loop, terminate early or skip.
# Break = terminates loop imediatley & move to nmext statement
#or Continue = skipd the rest of the code inside the loop for the current iteration and moves to the next iteration.

# i = 0
# # Break loop
# while i <= 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# i = 0
# # continue loop
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# text = "Dazza is awesome"
# vowels = "aeiouAEIOU"

# for each in text:
#     if each in vowels:
#         continue
#     print(each, end="") #the 'end="" prints output horizontally

# array = ["list","test","loop", "stop"]

# for each in array:
#     if each == "loop":
#         break
#     print(each)

# Nested loop
# a list of lists (matrix) or 2d list  etc
matrix = [
    [1,2,3],
    [9,8,7],
    [2,4,6]
]
# print(matrix[1])
# print(matrix[1][1])
# print(matrix[0][1])

for i in matrix:
    for item in i:
        print(item, end="")
    print()

for i in matrix:
    for item in i:
        if item == i[1]:
            print(item, end="")
    print()


