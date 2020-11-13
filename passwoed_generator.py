# This is a code to generate various passwords which are difficult to crack

import random
import string


class Passw:

    nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda']
    adjs = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']

    password = ""

    def __init__(self):
        self.password = ""

    def select(self):
        noun = random.choice(self.nouns)
        adj = random.choice(self.adjs)
        n = random.randrange(0, 100)
        p = random.choice(string.punctuation)

        self.password = noun + adj + str(n) + p

    def printp(self):
        print("password is ", self.password)


def main():
    print("\t\t\t\t WELCOME TO PASSWORD PICKER")

    ob = Passw()

    while True:
        ob.select()
        ob.printp()

        ch = input("Do you want to print another password")
        if ch.lower() == "no":
            break


if __name__ == "__main__":
    main()