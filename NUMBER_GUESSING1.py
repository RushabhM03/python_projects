# This program guesses the number inputted by the user

import random

attempts_l = []


def score():
    if len(attempts_l) == 0:
        print("There is no high score, please play the game to achieve one")
    else:
        print("The high score is ", min(attempts_l))


def start():
    print("\t\t\t\t\t HELLO, WELCOME TO THE GAME")
    for i in range(3):
        print()
    p_name = input("PLEASE ENTER YOUR NAME")
    st = input("HI {} DO YOU WANT TO PLAY (ENTER YES OR NO)".format(p_name))

    random_no = int(random.randint(1,10))
    attempts = 0

    score()

    while st.lower() == "yes":

        try:
            guess = int(input("Enter a number between 1 to 10"))
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")

            if int(guess) == random_no:
                print("THE NUMBER IS GUESSED CORRECTLY")
                attempts += 1
                attempts_l.append(attempts)
                print("It took you {} attempts".format(attempts))

                play_ag = input("WOULD YOU LIKE TO PLAY AGAIN(YES OR NO)")
                attempts = 0
                score()
                random_no = int(random.randint(1, 10))

                if play_ag.lower() == "no":
                    print("GAME OVER")
                    print("OK THANK YOU")
                    for i in range(2):
                        print()
                    break

            elif guess < random_no:
                print("The number is higher")
                attempts += 1

            elif guess > random_no:
                print("The number is lower")
                attempts += 1

        except ValueError as e:
            print("The value entered is not correct please try again")
            print("error is ",e)

    else:
        print("GAME OVER")


if __name__ == "__main__":
    start()