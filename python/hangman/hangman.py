# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.word = word.lower()
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.char = ""

        self.notFormattedMaskedWord = (["_" for c in range(len(self.word))])

    def guess(self, char):
        self.char = char.lower()
        if self.char not in self.word:
            self.remaining_guesses -= 1

        elif self.char in self.notFormattedMaskedWord:
            self.remaining_guesses -= 1

        if self.status == STATUS_WIN:
            raise ValueError("You are win! The game is over")

        if self.remaining_guesses < -1:
            raise ValueError("The game is already over.")

    def get_masked_word(self):

        for index, character in enumerate(self.word):
            if character == self.char:
                self.notFormattedMaskedWord[index] = self.char

        return "".join(self.notFormattedMaskedWord)

    def get_status(self):
        if self.remaining_guesses == -1:
            self.status = STATUS_LOSE
            return self.status

        if self.get_masked_word() == self.word:
            self.status = STATUS_WIN
            return self.status

        return self.status
