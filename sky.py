# This program implements turtle commands to draw a pictorial representation of the night sky

import turtle as t
from random import randint, random
from itertools import cycle


class Sky:

    def __init__(self):
        pass

    def backg(self):
        t.speed('fast')
        t.pensize(4)
        t.bgcolor('black')

    def star(self, points, size, col, x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

        angle = 180 - (180/points)

        t.color(col)
        t.begin_fill()

        for i in range(points):
            t.forward(size)
            t.right(angle)

        t.end_fill()


def main():
    ob = Sky()
    ob.backg()
    while True:
        ranPts = randint(2, 5) * 2 + 1
        ranSize = randint(10, 50)
        ranCol = (random(), random(), random())
        ranX = randint(-300, 300)
        ranY = randint(-250, 250)
        ob.star(ranPts, ranSize, ranCol, ranX, ranY)


if __name__ == "__main__":
    main()