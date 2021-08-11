def square(number):
    if number <= 0 or number > 64:
        raise ValueError("Please enter valid number")
    pointer = 1
    result = 1
    while number > pointer:
        result *= 2
        pointer += 1

    return result


def total():
    return sum([square(i) for i in range(1, 65)])
