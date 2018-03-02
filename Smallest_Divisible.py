# smallest number evenly divisible by 1 - 20
divisible = False
numb = 232792550
keep_going = True
i = 2

while divisible == False:
    keep_going = True
    print(numb)
    while keep_going == True and i <= 20:
        if numb % i != 0:
            keep_going = False
            numb += 1
            i = 2
        else:
            if i == 20:
                divisible = True
            i += 1
          
print(numb)