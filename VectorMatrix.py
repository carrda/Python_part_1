# Vector and Matrix List Exercises

# Multiply two equal length vectors -- could be any sizew

vector1 = [3, 4, -2]
vector2 = [5, 2, 1]

matrix1 = [[2, -2], [2,4]]
matrix2 = [[5]]
multiplyVector = []
 
for index in range(0, len(vector1)):
    multiplyVector.append(vector1[index] * vector2[index])

print("Example of vector multiplication")
print(str(vector1) + " X " + str(vector2) + " = " + str(multiplyVector))

# De-Dup a list -- remove duplicate entries
origList = [5, 3, 4, 5, 8]
noDupList = []
for item in origList:
    if item not in noDupList:
        noDupList.append(item)

print("Original list: " + str(origList))
print("Without dups: " + str(noDupList))
