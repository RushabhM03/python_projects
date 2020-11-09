# This is a simple calculator
# The following program is based on a simple calculator model
# all rights reserved

import math
import random


def add():
    print("ADDITION")
    n = int(input("ENTER THE FIRST NUMBER"))
    te = 0
    ans = n
    while n != 0:
        n = int(input("Enter another number and 0 to quit and show answer "))
        ans = ans + n
        te += 1
    return [ans, te]


def sub():
    print("SUBTRACTION")
    n = int(input("ENTER FIRST NUMBER"))
    te = 0
    ans = n
    while n != 0:
        n = int(input("Enter another number and 0 to quit and show answer"))
        ans = ans - n
        te += 1
    return [ans, te]


def mul():
    print("MULTIPLICATION")
    n = int(input("ENTER THE FIRST NUMBER"))
    te = 0
    ans = n
    while n != 0:
        n = int(input("Enter another number and 0 to quit and show answer "))
        ans = ans * n
        te += 1
    return [ans, te]


def div():
    print("DIVISION")
    n = int(input("ENTER FIRST NUMBER"))
    n1 = int(input("Enter second number"))
    ans = 0
    if n1 != 0:
        ans = n/n1
    else:
        print("CANNOT DIVIDE BY ZERO")
    return [ans]


def avg():
    print("AVERAGE OF NUMBERS")
    addi, nu = add()
    average = addi/nu
    return [average]


def sin():
    print("SINE OF ANGLE IN RAD")
    n = float(input("enter the number"))
    ans = math.sin(n)
    return [ans]


def cos():
    print("COSINE OF ANGLE IN RAD")
    n = float(input("enter the number"))
    ans = math.cos(n)
    return [ans]


def tan():
    print("TANGENT OF ANGLE IN RADS")
    n = float(input("enter the number"))
    ans = math.tan(n)
    return [ans]


def const():
    print("VALUES OF CONSTANTS")
    print("value of pi is ", math.pi)
    print("value of e is ", math.e)


def root():
    print("SQUARE ROOT")
    n = int(input("Enter a number"))
    ans = math.sqrt(n)
    return [ans]


def lg():
    print("LOGARITHM")
    n = int(input("enter a number"))
    b = int(input("enter base"))
    ans = math.log(n, b)
    return [ans]


def rd():
    print("PRINT A RANDOM NUMBER")
    a = int(input("enter first limit"))
    b = int(input("enter second limit"))
    ans = random.randint(a, b)
    return [ans]


def main():

    while True:

        list = []
        print(" \tWELCOME TO MY CALCULATOR")
        print(" \tSimple Calculator in python by Rushabh Maru")
        print(" \tEnter 1 for addition")
        print(" \tEnter 2 for subtraction")
        print(" \tEnter 3 for multiplication")
        print(" \tEnter 4 for division")
        print(" \tEnter 5 for average")
        print(" \tEnter 6 for sine")
        print(" \tEnter 7 for cosine")
        print(" \tEnter 8 for tangent")
        print(" \tEnter 9 to display math constants")
        print(" \tEnter 10 for square root")
        print(" \tEnter 11 for random number generator")
        print(" \tEnter 12 for quit")
        c = int(input(" "))
        print()

        if c != 12:
            if c == 1:
                list = add()
                print("Ans = ", list[0], " total inputs ", list[1])
                for i in range(2):
                    print()
            elif c == 2:
                list = sub()
                print("Ans = ", list[0], " total inputs ", list[1])
                for i in range(2):
                    print()
            elif c == 3:
                list = mul()
                print("Ans = ", list[0], " total inputs ", list[1])
                for i in range(2):
                    print()
            elif c == 4:
                list = div()
                print("Ans = ", list[0])
                for i in range(2):
                    print()
            elif c == 5:
                list = avg()
                print("Ans = ", list[0])
                for i in range(2):
                    print()
            elif c == 6:
                list = sin()
                print("Ans = ", list[0])
                for i in range(2):
                    print()
            elif c == 7:
                list = cos()
                print("Ans = ", list[0])
                for i in range(2):
                    print()
            elif c == 8:
                list = tan()
                print("Ans = ", list[0])
                for i in range(2):
                    print()
            elif c == 9:
                const()
                for i in range(2):
                    print()
            elif c == 10:
                list = root()
                print("Ans = ",list[0])
                for i in range(2):
                    print()
            elif c == 11:
                list = rd()
                print("Ans = ", list[0])
                for i in range(2):
                    print()
            else:
                print("Sorry, invalid character")
        else:
            for i in range(2):
                print()
            print("\t \tTHANK YOU FOR USING THIS CALCULATOR")
            print("\t \tPLEASE VISIT AGAIN")
            break


if __name__ == "__main__":
    main()
