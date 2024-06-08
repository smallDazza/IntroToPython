
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

guess_num = 5

users_guess = None
# while users_guess != guess_num:
#     users_guess = int(input("whats your guess( 1 to 10): "))

# print("correct")

while users_guess != guess_num:
    users_guess = int(input("whats your guess( 1 to 10): "))

    if users_guess < guess_num:
        print("to low")
    elif users_guess> guess_num:
        print("too high")
    else:
        print("correct")

# for loop