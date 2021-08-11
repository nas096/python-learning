i = 0
while True :
    user_input = input("Enter your word: ")
    for k in user_input:
        if k == 'q':
            i += 1
            break
        if k == "Q":
            i += 1
            break

''' answer:
while True:
    user_input = input('Type "q" or "Q" to quit: ')
    if user_input.upper() == "Q":
        break
'''