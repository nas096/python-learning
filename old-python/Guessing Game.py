
secret_words = "elephant"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_words and not(out_of_guesses): # dấu != là ko bằng
    if guess_count < guess_limit:
        guess = input("Enter a guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out out guesses, you lose!")
else:
    print("You guess a right word!")