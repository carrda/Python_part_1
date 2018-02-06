# List Exercises

# sum list of numbers
numList = [-1, -2, 2,5,7]
factorNum = 2 # will increase list items by factor of two
numTot = 0
largestNum = numList[0] # arbitrarily set starting largest number
smallestNum = numList[0] # same for smallest number
positiveList = []
factoredList = []

for item in numList:
    
    numTot = numTot + item
    
    if item > largestNum:
        largestNum = item
    
    if item < smallestNum:
        smallestNum = item

    if item % 2 == 0: # determine if item is even number
        print(str(item) + " is an even number.")

    if item > 0:
        print(str(item) + " is a positive number")
        positiveList.append(item) # build list of positive numbers

    factoredList.append(item * factorNum)

print("Total of numbers in list is " + str(numTot))
print("Largest number in list is " + str(largestNum))
print("Smallest number in list is " + str(smallestNum))
print("Here's the list of positive numbers.")
print(positiveList)
print("Here's the list multipled by " + str(factorNum))
print(factoredList)