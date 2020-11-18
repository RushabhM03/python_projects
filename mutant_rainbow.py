# Another program based on implementation of turtle graphics

import turtle as t
import random


class Mutantrain:

    pen_color = ['blue', 'red', 'yellow', 'green', 'white', 'pink', 'orange']

    def __init__(self):
        pass

    def bg(self):
        t.bgcolor('black')
        t.speed('fastest')
        t.shape('turtle')
        t.fillcolor('green')

    def inside_win(self):
        left_limit = (-t.window_width() / 2) + 100
        right_limit =(t.window_width() / 2) - 100
        top_limit = (t.window_height() / 2) - 100
        bottom_limit = (-t.window_height() / 2) + 100

        (x, y) = t.pos()
        inside = left_limit < x < right_limit and bottom_limit < y < top_limit
        return inside

    def line(self, len, wid):
        t.pensize(wid)
        while True:
            pc = (random.choice(self.pen_color))
            t.pencolor(pc)

            t.fillcolor(random.choice(self.pen_color))
            t.shapesize(2, 2, 1)
            t.stamp()

            if self.inside_win():

                angle = random.randint(1, 180)
                t.right(angle)
                t.forward(len)
            else:
                t.backward(len)


def main():

    ob = Mutantrain()
    ob.bg()

    len = input("Enter the length of the line (long, medium, small)")
    if len.lower() == "long":
        linel = 250
    elif len.lower() == "medium":
        linel = 200
    elif len.lower() == "small":
        linel = 150
    else:
        print("Enter a proper choice")

    wid = input("Enter the width of the line (thick, medium, thin)")
    if wid.lower() == "thick":
        width = 50
    elif wid.lower() == "medium":
        width = 40
    elif wid.lower() == "thin":
        width = 30
    else:
        print("Enter a proper choice")

    ob.line(linel, width)


if __name__ == "__main__":
    main()
