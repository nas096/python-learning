"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

from math import sqrt

# check if a number is prime.

def isPrime(number):
    if number < 2:
        return False
    
    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            return False
    return True

# Generate the list of 10001 prime number
    
j = 2
primesList = []
while True:
    if isPrime(j):
        primesList.append(j)
        j += 1
    else:
        j += 1

    if len(primesList) == 10001:
        break

print(primesList[10000])