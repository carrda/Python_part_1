# Collatz Conjecture
n = int(input("Enter a postive integer: "))
print("n = {}".format(n))

while n != 1:
    if n % 2 == 0:
        n = int(n / 2)
        print(n)
    else:
        n = (n * 3) + 1
        print(n)