"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""


def ifNIsEven(number):
    return number//2


def ifNIsOdd(number):
    return 3*number + 1


NUMBER = 1_000_000

has2 = {}


def collatz(num):
    count = 1
    temp = num

    while temp > 1:
        if temp % 2 == 0:
            temp = ifNIsEven(temp)
            if temp in has2:
                count += has2[temp]
                break
            else:
                count += 1

        else:
            temp = ifNIsOdd(temp)
            if temp in has2:
                count += has2[temp]
                break

            else:
                count += 1
    has2[num] = count  # Record the previous result to dictionary

    return count


num = 0
greatest = 0

for theNumber in range(NUMBER):
    sequenceLen = collatz(theNumber)
    if num < sequenceLen:
        num = sequenceLen
        greatest = theNumber
print(greatest)
