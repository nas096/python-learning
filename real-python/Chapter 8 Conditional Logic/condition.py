user_input = input("Enter a word:")
if len(user_input) < 5:
    print("Your word has less than 5 char")
if len(user_input) == 5:
    print("Your word has 5 char")
if len(user_input) > 5:
    print("Your word has greater than 5 char")