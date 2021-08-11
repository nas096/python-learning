"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
number = 0
from math import sqrt
from typing import Tuple
def isPrime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number > 2 and number % 2 == 0:
        return False

    max_div = int(sqrt(number))
    for i in range(3, max_div+1, 2):
        if number % i == 0:
            return False
    
    return True

# Sieve method
def primeSieve(number):
    sieves = [True for i in range(number+1)]

    sieves[0] = False
    sieves[1] = False

    # create the sieve
    for i in range(2, int(sqrt(number))+1):
        pointer = i*2
        while pointer < number:
            sieves[pointer] = False
            pointer += i


    primes = [i for i in range(number) if sieves[i] == True]

    return primes






NUMBER = 2_000_000
def main():
    primeList = [i for i in range(1, NUMBER) if isPrime(i)]
    return sum(primeList)

if __name__ == "__main__":
    print(sum(primeSieve(NUMBER)))
    # print(main())
    pass