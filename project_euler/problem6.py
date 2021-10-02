"""The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

first100numbers = [i for i in range(1, 101)]
# Find the sum of the squares of first 100 natural numbers
def sumOfSquares(numlist):
    squaresList = [number*number for number in numlist]
    return sum(squaresList)

# Find the square of the sum of the first 100 natural numbers
def squareOfSum(numlist):
    sumNumbers = sum(numlist)
    return sumNumbers*sumNumbers
    pass

# Find the difference between 2 of them.
if __name__ == "__main__":
    print(squareOfSum(first100numbers)-sumOfSquares(first100numbers))