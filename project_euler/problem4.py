"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""


import math

# Find the the number pair that makes palindrome
palindromePair = []
for i in range(100,1000):
    for j in range(100, 1000): 
        originalNumber = i * j
        reversedNumber = int((str(originalNumber)[::-1]))
        if originalNumber == reversedNumber:
            palindromePair.append((i,j))

# Calculate the palindrome
palindromeList = []
for first, second in palindromePair:
    palindromeList.append(first*second)

# Find the largest palindrom
print(max(palindromeList))