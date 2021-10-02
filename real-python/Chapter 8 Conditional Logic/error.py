while True:
    try:
        user = int(input('Enter a integer: '))
    except ValueError:
        print("Please try again")
        continue
    else:
        break