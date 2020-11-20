# This file runs a countdown timer

import time


class Timer:

    def __init__(self, t):
        self.t = t

    def count(self):
        while self.t:
            mins, secs = divmod(self.t, 60)
            timer1 = "{:02d}:{:02d}".format(mins, secs)
            print(timer1)
            time.sleep(1)
            self.t -= 1

        print('Fire in the hole!!')


def main():
    t = int(input("Enter timer limit"))
    obj = Timer(t)
    obj.count()


if __name__ == "__main__":
    main()