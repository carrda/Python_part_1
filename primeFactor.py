# Find largest prime factor of a given number (big_number)

big_number = 600851475143
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
#print(known_primes)

# div_by_prime = False

while n <= int(big_number / 2):
    if is_prime(n) == True:
        if big_number % n == 0:
            large_Factor = n
            print(large_Factor)
  
    n = n + 1

    
print("Largest prime factor of {} is: {}".format(big_number, large_Factor))