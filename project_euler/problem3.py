"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

import math
import logging
number = 600851475143 
# number = 493 # For testing only
# Getting factors of a number

def getFactor(num):

	factors = []
	for potentialFactor in range(1, int(math.sqrt(num))):
		if num % potentialFactor == 0:
			factors.append(potentialFactor)
			factors.append(num // potentialFactor)

	return factors

print(getFactor(4))
# Determine if a number is prime.

def isPrime(num):
	return len(getFactor(num)) == 2


# Find the highest number
allFactors = getFactor(number)

allPrimeFactors = [factor for factor in allFactors if isPrime(factor)]
print(max(allPrimeFactors))
