# This program  prints a calendar based on the particular month and year entered by the user

import calendar


class cal:

    yy = 0
    mm = 0

    def __init__(self):
        self.yy = 0
        self.mm = 0

    def inp(self):

        while True:
            self.yy = input("Enter the year")
            self.mm = input("Enter the month (Enter 0 to display the calendar of the entire year")

            if len(self.yy) == 4 and 0 < int(self.mm) < 13:
                self.disp_mth()
                break

            elif len(self.yy) == 4 and int(self.mm) == 0:
                self.disp_yr()
                break

            else:
                print("Invalid credentials for month and year")

    def disp_mth(self):
        for i in range(4):
            print()
        print(calendar.month(int(self.yy), int(self.mm)))

    def disp_yr(self):
        for i in range(4):
            print()
        print(calendar.calendar(int(self.yy)))


def main():
    ob = cal()

    print("\t\t\t WELCOME TO CALENDAR")

    for i in range(5):
        print()

    print("PRESS 1 TO START")
    o = int(input())

    if o == 1:
        ob.inp()
    else:
        print("PLEASE RESTART THE PROGRAM AND TRY AGAIN")
        exit(0)


if __name__ == "__main__":
    main()
