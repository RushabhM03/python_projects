# This program is a basic game of a standard rock, paper, scissor game

import random
import re


class Rps:

    def __init__(self):
        pass

    def game(self):
        while True:
            print("Enter your weapon of choice")
            print("[R]ock\t[P]aper\t[S]cissor")
            w = input()

            if not re.match("[RrSsPp]", w):
                print("Please enter a proper choice")
                continue

            print("Your choice = ", w)

            choices = ['R', 'P', 'S']
            oc = random.choice(choices)

            print("AI's choice = ", oc)
            print()

            if oc == w.upper():
                print("TIE")
            elif oc == "R" and w.upper() == "S":
                print("I WIN")
            elif oc == "P" and w.upper() == "R":
                print("I WIN")
            elif oc == "S" and w.upper() == "P":
                print("I WIN")
            else:
                print("YOU WIN")

            pa = input("DO YOU WANT TO PLAY AGAIN (YES) OR (NO)")
            if pa.upper() == "NO":
                print("THANK YOU FOR PLAYING")
                break
            elif pa.upper() == "YES":
                continue
            else:
                print("Enter a proper value and restart the program")
                exit(0)


def main():
    print("\t\t\t WELCOME TO ROCK PAPER SCISSORS")
    for i in range(5):
        print()

    ob = Rps()
    ob.game()


if __name__ == "__main__":
    main()
