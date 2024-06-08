
# stars = 5

# for i in range(1, stars+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

string_list = ["Dazza", "Steve","Wayne","luke", "Callum","Aaron"]
result = 0

for string in string_list:
    for letter in string:
        if letter in 'aeiouAEIOU':
            result += 1
print("the total of occuring letter is:", result)
