"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

# My method
def isPyTriplet(a, b, c):
    return (a**2 + b**2) == c**2

def main():
    for a in range(1,1001):
        for b in range(1, 1001):
            c = 1000 - a - b
            if isPyTriplet(a,b,c):
                return a*b*c

# Dickson's method

def pyTripletDickson():
    for r in range(1, 1000):
        for s in range(1, r):
            if (r**2/2)%s == 0:
                t = (r**2/2)/s
                if r+s+r+t+r+s+t == 1000:
                    return(r+s)*(r+t)*(r+s+t)

# m, n formula
def mnFormula():
    for m in range(1, 1000):
        for n in range(1, m):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            if a + b + c == 1000:
                return a*b*c
if __name__ == "__main__":

    print(pyTripletDickson())
    print((mnFormula()))
    print(main())
