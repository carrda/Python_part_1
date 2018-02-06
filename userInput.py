name = input("What is your name? ")
print("Hello, " + name + "!")
print("HELLO, " + name.upper() + "!")
print("Please fill in th eblanks below:")
print("----(name)---\'s favorite subject in school is ----(subject)----.")
name2 = input("What is name? ")
subject = input("What is subject? ")
print(name2 + "\'s favorite subject in school is " + subject + ".")
dayNum = int(input("Day (0-6)? "))
if dayNum == 0:
    print("Sunday")
elif dayNum == 1:
    print("Monday")
elif dayNum == 2:
    print("Tuesday")
elif dayNum == 3:
    print("Wednesday")
elif dayNum == 4:
    print("Thursday")
elif dayNum == 5:
    print("Friday")
elif dayNum == 6:
    print("Saturday")
else:
    print("You entered invalid number.")

dayNum = int(input("Day (0-6)? "))
if dayNum == 0 or dayNum ==6:
    print("Sleep in")
elif dayNum == 1 or dayNum == 2 or dayNum == 3 or dayNum == 4 or dayNum == 5:
    print("Go to work")
else:
    print("You entered invalid number.")