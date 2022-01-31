# primes
import math
import random

def finding_prime(number):
    num = abs(number)

    if num < 4: return True

    for x in range(2, num):
        if num % x == 0:
            return False

    return True

def finding_prime_sqrt(number):
    num = abs(number)

    if num < 4: return True

    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True

def finding_prime_fermat(number):
    if number <= 102:
        for a in range(2, number):
            if pow(a, number - 1, number) != 1:
                return False
        return True
    
    else:
        for i in range(100):
            a = random.randint(2, number - 1)
            if pow(a, number - 1, number) != 1:
                return False
        return True

def finding_prime_sieve(number):
    n = abs(number)
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False

        p += 1
    prime[0] = False
    prime[1] = False
    
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            print(p)

def test_finding_prime():
    number1 = 17
    number2 = 20

    assert(finding_prime(number1) == True)
    assert(finding_prime(number2) == False)
    assert(finding_prime_sqrt(number1) == True)
    assert(finding_prime_sqrt(number2) == False)
    assert(finding_prime_fermat(number1) == True)
    assert(finding_prime_fermat(number2) == False)

    print('Tests passed!')

if __name__ == '__main__':
    test_finding_prime()
