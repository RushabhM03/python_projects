# This is a sample program to build a robot using turtle commands

import turtle as t


class Rbt:

    def rectangle(self, horizontal, vertical, color):
        t.pendown()
        t.pensize(1)
        t.color(color)
        t.begin_fill()

        for i in range(2):
            t.forward(horizontal)
            t.right(90)
            t.forward(vertical)
            t.right(90)

        t.end_fill()
        t.penup()

    def bg(self):
        t.penup()
        t.speed('slow')
        t.bgcolor('Dodger blue')

    def foot(self):
        t.goto(-100, -150)
        self.rectangle(50, 20, 'blue')
        t.goto(-30, -150)
        self.rectangle(50, 20, 'blue')

    def legs(self):
        t.goto(-25, -50)
        self.rectangle(15, 100, 'grey')
        t.goto(-55, -50)
        self.rectangle(-15, 100, 'grey')

    def body(self):
        t.goto(-90, 100)
        self.rectangle(100, 150, 'red')

    def arms(self):
        t.goto(-150, 70)
        self.rectangle(60, 15, 'grey')
        t.goto(-150, 110)
        self.rectangle(15, 40, 'grey')
        t.goto(10, 70)
        self.rectangle(60, 15, 'grey')
        t.goto(55, 110)
        self.rectangle(15, 40, 'grey')

    def neck(self):
        t.goto(-50, 120)
        self.rectangle(15, 20, 'grey')

    def head(self):
        t.goto(-85, 170)
        self.rectangle(80, 50, 'red')

    def eyes(self):
        t.goto(-60, 160)
        self.rectangle(30, 10, 'white')
        t.goto(-60, 160)
        self.rectangle(5, 5, 'black')
        t.goto(-45, 155)
        self.rectangle(5, 5, 'black')

    def mouth(self):
        t.goto(-65, 135)
        t.right(5)
        self.rectangle(40, 5, 'black')


def main():
    ob = Rbt()
    ob.bg()
    ob.arms()
    ob.body()
    ob.foot()
    ob.foot()
    ob.legs()
    ob.neck()
    ob.head()
    ob.eyes()
    ob.mouth()
    t.hideturtle()


if __name__ == "__main__":
    main()