# This project is based on the traditional game of hand cricket

import random


class Hc:

    def __init__(self):
        self.set = [1, 2, 3, 4, 5, 6]
        self.u_score = 0
        self.c_score = 0

    def start(self):
        uc = 0
        self.u_score = 0
        self.c_score = 0
        print("IT IS YOUR BATTING")

        try:
            print("Enter a number between 1 and 6")
            uc = int(input())
        except ValueError as e:
            print("Enter a proper value")
            print("ERROR = ", e)
            uc = 0

        cc = random.choice(self.set)
        if 0 < uc < 7:
            print("Your choice = ", uc)
            print("Computer's choice = ", cc)
        else:
            print("please enter a number between 1 and 6 only")

        while uc != cc:
            if 0 < uc < 7:
                self.u_score += uc

            try:
                print("Enter a number between 1 and 6")
                uc = int(input())
            except ValueError as e:
                print("Enter a proper value")
                print("ERROR = ", e)
                uc = 0

            cc = random.choice(self.set)
            if 0 < uc < 7:
                print("Your choice = ", uc)
                print("Computer's choice = ", cc)
            else:
                print("please enter a number between 1 and 6 only")
        else:
            print("You are out")
            print("Your score is ", self.u_score)

        print("*************************************************************************************************")
        print("Your innings is over")
        for i in range(5):
            print()
        print("NOW YOU WILL BOWL")

        try:
            print("Enter a number between 1 and 6")
            uc = int(input())
        except ValueError as e:
            print("Enter a proper value")
            print("ERROR = ", e)
            uc = 0

        cc = random.choice(self.set)
        if 0 < uc < 7:
            self.c_score += cc
            print("Your choice = ", uc)
            print("Computer's choice = ", cc)
        else:
            print("please enter a value between 1 and 6 only")
            cc = 0
            uc = 0

        while uc != cc and self.c_score < self.u_score:
            try:
                print("Enter a number between 1 and 6")
                uc = int(input())
            except ValueError as e:
                print("Enter a proper value")
                print("ERROR = ", e)
                cc = 0
                uc = 0

            cc = random.choice(self.set)

            if 0 < uc < 7:
                self.c_score += cc
                print("Your choice = ", uc)
                print("Computer's choice = ", cc)
            else:
                print("Enter a number between 1 and 6 only")
        else:
            if uc == cc:
                print("The computer is out")
            print("The computer's score is ", self.c_score)

        self.score()
        self.check()

        for i in range(50):
            print()

    def score(self):
        print("Your score is ", self.u_score)
        print("Computer's score is", self.c_score)

    def check(self):
        if self.c_score > self.u_score:
            print("You lost")
        elif self.u_score > self.c_score:
            print("You won")
        else:
            print("Its a tie")


def main():
    ob = Hc()

    print("\t\t\t WELCOME TO HAND CRICKET")
    for i in range(5):
        print()

    ob.start()
    c = 0
    while True:
        try:
            c = int(input("Enter 1 to play again else enter any number to quit"))
        except ValueError as e:
            print("Enter a proper number ")
            print(e)
        if c == 1:
            ob.start()
        else:
            print("Thank you")
            exit(0)
            break


if __name__ == "__main__":
    main()

# End of program
