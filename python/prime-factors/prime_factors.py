from math import sqrt


def factors(value):
    # If value is even
    result = []
    while value % 2 == 0:
        result.append(2)
        value = value / 2

    # If value is odd
    for i in range(3, int(sqrt(value)+1), 2):
        while value % i == 0:
            result.append(i)
            value = value / i

    if value > 2:
        result.append(value)
    return result
