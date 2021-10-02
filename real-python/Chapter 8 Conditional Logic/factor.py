user_factor = int(input('Enter a positive integer: '))
ending_range = user_factor + 1
for i in range(1, ending_range):
    if (user_factor % i == 0):
        print(f'{i} is the factor of {user_factor}')