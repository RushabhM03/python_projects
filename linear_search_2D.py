# This program performs linear search algorithm on a 2D array


from numpy import *


class Srch2d :

    def __init__(self,x):
        self.x = x

    def disp(self,x,n,m):
        print("THE array entered is")
        for i in range(n):
            for j in range(m):
                print(self.x[i][j])

    def srch(self,x,n,m,item):
        flag = False
        i = 0
        j = 0
        for i in range(n):
            for j in range(m):
                if self.x[i][j] == item:
                    flag = True
                    break
        return flag,i,j


def main():
    try:
        n = int(input("Enter the no of rows"))
        m = int(input("Enter the no of columns"))

        a = zeros((n, m), dtype=int)

        for i in range(n):
            for j in range(m):
                x = int(input("Enter element"))
                a[i][j] = x

        item = int(input("Enter the element to be searched"))

        ob = Srch2d(a)

        ob.disp(a, n, m)
        f, b, c = ob.srch(a, n, m, item)

        if f:
            print("Element found at ", b, " ", c)
        else:
            print("Not found please try again")

    except ValueError as e:
        print("Please enter proper values")
        print("error = ", e)

        for i in range(4):
            print()


if __name__ == "__main__" :
    main()