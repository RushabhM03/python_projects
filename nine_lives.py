# NINE LIVES PROGRAM

import random


class nine:

    words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane', 'phone', 'pasta', 'table']
    sc_wrd = random.choice(words)

    clue = ['?', '?', '?', '?', '?']
    ht = u'\u2764'
    guessed_word_correctly = False

    df = input("Enter difficulty level (EASY(e),MEDIUM(m),HARD(h))")
    if df.lower() == "e":
        lives = 12
    elif df.lower() == "m":
        lives = 9
    elif df.lower() == "h":
        lives = 6

    def clue_up(self, guess_lt, clue, sc_wrd):
        i = 0
        while i < len(sc_wrd):
            if guess_lt == sc_wrd[i]:
                clue[i] = guess_lt
            i += 1

    def live(self):
        while self.lives > 0:
            print('Lives left: ' + self.ht * self.lives)
            guess = input('Guess a letter or the whole word: ')
            if guess == self.sc_wrd:
                self.guessed_word_correctly = True
                break

            if guess in self.sc_wrd:
                self.clue_up(guess, self.clue, self.sc_wrd)
            else:
                print('Incorrect. You lose a life')
                self.lives = self.lives - 1

    def check(self):
        if self.guessed_word_correctly:
            print('You won! The secret word was ' + self.sc_wrd)
        else:
            print('You lost! The secret word was ' + self.sc_wrd)


def main():
    ob = nine()
    print("WELCOME TO NINE LIVES")
    ob.live()
    ob.check()


if __name__ == "__main__":
    main()