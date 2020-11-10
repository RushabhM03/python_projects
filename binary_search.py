# This program performs binary search algorithm

from array import *

pos = -1


class BSearch:

    def __init__(self, x):
        self.x = x

    def find(self, item, l):
        lb = 0
        ub = l-1
        flag = False

        while lb <= ub :
            mid = (lb+ub)//2

            if self.x[mid] == item:
                flag = True
                pos = mid
                break

            elif self.x[mid] > item :
                ub = mid-1

            else:
                lb = mid+1
        return flag


def main():
    l = int(input("Enter the length of the array"))
    a = array('i', [])

    for i in range(l):
        x = int(input("Enter the element"))
        a.append(x)

    item = int(input("Enter the item to be searched"))

    ob = BSearch(a)
    f = ob.find(item,l)

    if f:
        print("found at position ",pos)

    else:
        print("not found pls try again")


if __name__ == "__main__":
    main()