import turtle as t

from itertools import cycle


class Ss:

    colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white'])

    def __init__(self):
        pass

    def circle(self, size, angle, shift):
        t.pencolor(next(self.colors))
        t.circle(size)
        t.right(angle)
        t.forward(shift)
        self.circle(size + 5, angle + 1, shift + 1)


def main():
    ob = Ss()
    t.bgcolor('black')
    t.speed('fast')
    t.pensize(4)
    t.pendown()
    ob.circle(30, 0, 1)


if __name__ == "__main__":
    main()