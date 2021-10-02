string_input = input('Enter a string: ')
while True:
    try:
        number_input = int(input("Enter an index: "))
        print(string_input[number_input])
    except ValueError:
        print("Please enter a number")
        continue
    except IndexError:
        print("Please enter a valid index")
        continue
    else:
        break