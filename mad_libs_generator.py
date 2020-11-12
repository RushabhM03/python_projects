# This program accepts word as in nouns, pronouns ,etc and creates madlibs


class madlibs:

    def __init__(self, op):
        self.op = op

    def generate(self, noun1, noun2, noun3, p_noun, adj, place):
        print("------------------------------------------")
        print("Be kind to your", noun1, "- footed", p_noun)
        print("For a duck may be somebody's", noun2, ",")
        print("Be kind to your", p_noun, "in", place)
        print("Where the weather is always", adj, ".")
        print()
        print("You may think that is this the", noun3, ",")
        print("Well it is.")
        print("------------------------------------------")


def main():

    print("\t \t \t \t WELCOME TO MAD LIBS")
    op = input("Would you like to play (YES/NO)")

    try:
        while op.lower() == "yes":
            noun1 = input("Enter a noun")
            noun2 = input("Enter the second noun")
            noun3 = input("Enter a third noun")
            p_noun = input("Enter a plural noun")
            adj = input("Enter an adjective")
            place = input("Enter a place")

            obj = madlibs(op)
            obj.generate(noun1, noun2, noun3, p_noun, adj, place)

            op = input("Would you like to play (YES/NO)")

        else:
            print("thank you for playing")

    except Valueerror as e:
        print("please enter the correct value")
        print(e)


if __name__ == "__main__":
    main()