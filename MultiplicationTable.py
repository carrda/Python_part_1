# print out multiplication table for 1 to 10
# 1 X 1 = 1
# 1 X 2 = 2
# 10 X 8 = 80
# 10 X 9 = 90
# 10 X 10 = 100

for firstNum in range(1, 11):
    for secondNum in range(1,11):
        print(str(firstNum) + " X " + str(secondNum) + " = " + str(firstNum * secondNum))