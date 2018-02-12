# print box with height & width inputs
boxWidth = int(input("Width? "))
boxHeight = int(input("Height? "))

for iHeight in range(1, boxHeight + 1):
    if iHeight == 1 or iHeight == boxHeight:
        print('*' * boxWidth)
    else:
        print('*' + (boxWidth - 2) * ' ' + '*')

# print a triange with height an input

triangleHeight = int(input("Height? "))

for line in range(1, triangleHeight + 1):
    print((triangleHeight - line) * ' ' + '*'+ ((line - 1) * 2) * '*' + (triangleHeight - line) * ' ')

# print out multiplication table for 1 to 10
# 1 X 1 = 1
# 1 X 2 = 2
# 10 X 8 = 80
# 10 X 9 = 90
# 10 X 10 = 100

for firstNum in range(1, 11):
    for secondNum in range(1,11):
        print(str(firstNum) + " X " + str(secondNum) + " = " + str(firstNum * secondNum))

