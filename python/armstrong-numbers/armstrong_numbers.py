def is_armstrong_number(number):
    numberLen = len(str(number))
    if numberLen == 1:
        return True

    numberList = [int(i) for i in str(number)]

    armstrongNumber = [i**numberLen for i in numberList]

    if sum(armstrongNumber) == number:
        return True
    return False

    # This is the built-in function
    # return is_armstrong_number(number)
