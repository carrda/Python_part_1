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