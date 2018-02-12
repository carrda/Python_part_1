# Find the 10,001st (or nth) prime number

which_Prime = 10001
prime_Counter = 2

n = 4
known_primes = [2,3]

def is_prime(n):
    total_primes = len(known_primes)
    for i in range(0,total_primes):
        if(n % known_primes[i] == 0):
            # NOT PRIME!!
            return False
        else:
            # it might be prime, it might not. 
            # Its just not divisible by this number
            continue
    known_primes.append(n)
    return True


while prime_Counter < which_Prime:
    if is_prime(n) == True:
        prime_Counter += 1
  
    n = n + 1

    
print("The {} number prime number is: {}".format(prime_Counter, n - 1))