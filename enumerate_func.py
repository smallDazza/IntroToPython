

## enumerate() function = finds the index and value in a list

animals = ["cat","dog","bird","frog","horse","fish"]

target = "frog"

for  index, animal in enumerate(animals):
    #print( index, animal)
    if animal == target:
        print(index, animal)
        break

