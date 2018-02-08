# Loop Exercises

# print 1 to 10
for i in range(1, 11):
    print(i)

# custom range base on user input
startNum = input("Start from: ")
endNum = input("End on: ")

for i in range(int(startNum), int(endNum) + 1):
    print(i)

# print odd numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 1:
        print(i)

# print 5 X 5 square of '*' characters
for i in range(1, 6):
    print(5 * '*')

# print custom square based on input
squareSize = input("How big is the square? ")
for i in range(1, int(squareSize) + 1):
    print(int(squareSize) * '*')

# print box with height & width inputs
boxWidth = int(input("Width? "))
boxHeight = int(input("Height? ")

for iHeight in range(1, boxHeight + 1):
    for iWidth in range