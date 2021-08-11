import random
nums_digit = 3


guesses = 10

def main():

	print(f'''      Bagels, a deductive logic game.
I am thinking of a {nums_digit}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
	Pico         One digit is correct but in the wrong position.
	Fermi        One digit is correct and in the right position.
	Bagels       No digit is correct.
For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.''')
	while True:

		secret_number = getSecretNumber()
		print("I have thought up a number")
		print(f"You have {guesses} to get it")

		numGuesses = 1

		while numGuesses <= guesses:

			user_guess = ''
			while not user_guess.isdecimal() or len(user_guess) != nums_digit:
			# Check user's guess
				print(f"Guess #{numGuesses}")
				user_guess = (input("> "))



			clue = getClues(user_guess, secret_number)
			print(clue)
			numGuesses += 1

			if user_guess == secret_number:
				break
			if numGuesses > guesses:
				print("You are out of guesses")
				print(f"The answer is {secret_number}")
		print("Do you want to try again? (yes or no)")

		if not input("> ").lower().startswith("y"):
			break

	print("Thanks for playing")

def getSecretNumber():
	numbers_order = list("0123456789")
	random.shuffle(numbers_order)
	secret_number = ""
	for i in range(nums_digit):
		secret_number += str(numbers_order[i])

	return secret_number

def getClues(user_guess, secret_number):
	clue = []
	if user_guess == secret_number:
		return "You got it!"

	for i in range(len(user_guess)):
		if user_guess[i] == secret_number[i]:
			clue.append("Fermi")
		elif user_guess[i] in secret_number:
			clue.append("Pico")

	if len(clue) == 0:
		return "Bagels"
	else:
		clue.sort()
		return " ".join(clue)		 
if __name__ == '__main__':
	main()