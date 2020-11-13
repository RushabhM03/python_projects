# This is sample template program that calculates a score based on the no of correct questions answered

import time


class quiz:

    score = 0

    def __init__(self):
        self.score = 0

    def print_sc(self):
        print("YOUR SCORE IS ", self.score)

    def quiz(self):
        print("Question 1")
        print("Which is the fastest animal")
        a1 = input("Enter answer   ")
        if a1.lower() == "cheetah" :
            self.score += 1

        print("Question 2")
        print("Which is the third planet")
        a1 = input("Enter answer   ")
        if a1.lower() == "earth":
            self.score += 1

        print("Question 3")
        print("sum of first ten numbers")
        a1 = input("Enter answer   ")
        if int(a1) == 55:
            self.score += 1

        print("Question 4")
        print("which language is this")
        a1 = input("Enter answer   ")
        if a1.lower() == "python":
            self.score += 1

        print("Question 5")
        print("what is the national sport of india")
        a1 = input("Enter answer   ")
        if a1.lower() == "hockey":
            self.score += 1


def main():

    obj = quiz()

    print("WELCOME TO QUIZ")
    o = input("Do you want to play")

    if o.lower() == "yes":
        obj.quiz()
        for i in range(5):
            print()

        obj.print_sc()

    else:
        print("OK PLEASE TRY AGAIN")


if __name__ == "__main__":
    main()
