"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

# A function that finds the greatest common multiple
def gcd(number1, number2):
    if number2 == 0:
        return number1
    else:
        return gcd(number2, number1%number2)

# Find the least common multiple
if __name__ == "__main__":
    lcm = 1
    for i in range(1,21):
        lcm *= i//gcd(lcm, i)
    
    print(lcm)

