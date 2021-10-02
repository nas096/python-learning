def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction:
    def __init__(self, numerator, denominator):
        # Sentence 6 solution
        if numerator.is_integer() == False or denominator.is_integer() == False:
            raise ValueError("Your numerator and denominator must be integer.")

        if denominator < 0:
            self.num = -abs(numerator)
            self.den = abs(denominator)

        common = gcd(numerator, denominator)
        self.num = numerator // common
        self.den = denominator // common

    def __str__(self):
        return f"{self.num}/{self.den}"

    # 9 solution
    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"

    # Sentence 2 Solution
    def __add__(self, frac):
        new_num = self.num*frac.den + self.den*frac.num
        new_den = self.den*frac.den
        return Fraction(new_num, new_den)
    # 1.17 Sentence 3 solution

    def __sub__(self, frac):
        new_num = self.num*frac.den - self.den*frac.num
        new_den = self.den*frac.den
        return Fraction(new_num, new_den)

    def __mul__(self, frac):
        new_num = self.num*frac.num
        new_den = self.den*frac.den
        return Fraction(new_num, new_den)

    def __truediv__(self, frac):
        new_num = self.num//frac.num
        new_den = self.den//frac.den
        return Fraction(new_num, new_den)

    # Sentence 4 solution

    def __gt__(self, frac):
        common = gcd(frac.den, self.den)
        frac1num = common*self.num
        frac2num = common*frac.num
        return frac1num > frac2num

    def __ge__(self, frac):
        common = gcd(frac.den, self.den)
        frac1num = common*self.num
        frac2num = common*frac.num
        return frac1num >= frac2num

    def __lt__(self, frac):

        common = gcd(frac.den, self.den)
        frac1num = common*self.num
        frac2num = common*frac.num
        return frac1num < frac2num

    def __le__(self, frac):
        common = gcd(frac.den, self.den)
        frac1num = common*self.num
        frac2num = common*frac.num
        return frac1num <= frac2num

    def __ne__(self, frac):
        common = gcd(frac.den, self.den)
        frac1num = common*self.num
        frac2num = common*frac.num
        return frac1num != frac2num
    # Sentence 7 solution

    def __radd__(self, frac):
        if frac == 0:
            return self
        else:
            frac = Fraction(frac, 1)
            return self.__add__(frac)

    # Sentence 8 Solution
    def __iadd__(self, frac):
        if isinstance(frac, int):
            frac = Fraction(frac, 1)

        return self.__add__(frac)

    def lowestTerms(self):
        common = gcd(self.num, self.den)
        return Fraction(self.num//common, self.den//common)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den


frac1 = Fraction(1, 2)
frac2 = Fraction(5, 6)
