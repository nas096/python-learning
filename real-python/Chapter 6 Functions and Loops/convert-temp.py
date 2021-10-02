def convert_cel_to_far():
    while True:
        try:
            cel = int(input('Enter a temperature in degrees F: '))
        except ValueError:
            print('Please try again')
            continue
        else:
            return (f'{cel} degrees C = {float(cel * 9/5 + 32):.2f} degrees F')
def convert_far_to_cel():
    while True:
        try:
            far = int(input('Enter a temperature in degrees C: '))

        except ValueError:
            print("Please Try Again")
            continue
        else:
            return (f'{far} degrees F = {float((far - 32) * 5/9):.2f} degrees C')


print(convert_far_to_cel())
print(convert_cel_to_far())