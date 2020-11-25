# This is a banking project


class Account:
    def __init__(self, username, password, amount):
        self.username = username
        self.password = password
        self.amount = amount

    def __repr__(self):
        return f"Account({self.username}, {self.password})"


class BankSystem:
    def __init__(self):
        self.accounts = []

    def create_account(self, username, password, amount):
        for i in self.accounts:
            if i.username == username:
                return "USERNAME ALREADY EXISTS"

        new = Account(username, password, amount)
        self.accounts.append(new)
        return "Account created successfully"

    def get_account(self, username, password):
        for i in self.accounts:
            if i.username == username and i.password == password:
                return i
        else:
            return False

    def withdraw(self, username, password, amount):
        account = self.get_account(username, password)

        if account == False:
            return "INVALID CREDENTIALS"

        if amount > account.amount:
            return "INSUFFICIENT BALANCE"

        if amount > 0:
            account.amount -= amount
            return "WITHDRAWN SUCCESSFULLY", account.amount

        else:
            return "INVALID ACCOUNT"

    def deposit(self, username, password, amount):
        account = self.get_account(username, password)

        if account == False:
            return "INVALID CREDENTIALS"

        if amount > 0:
            account.amount += amount
            return "DEPOSIT SUCCESSFULLY", account.amount

        else:
            return "INVALID ACCOUNT"


def main():

    print("\t\t\t WELCOME TO MY BANK")
    for i in range(10):
        print()

    BANK = BankSystem()

    print("PLEASE CREATE AN ACCOUNT TO PROCEED FURTHER")

    username = input("Enter username")
    password = input("Enter password")
    amount = int(input("Enter amount"))

    output = BANK.create_account(username, password, amount)
    print(output)

    while True:
        for i in range(5):
            print()

        print("Enter 'a' to proceed to deposit ")
        print("Enter 'b' to withdraw")
        print("Enter anything else to quit")
        o1 = input()

        if o1.lower() == "a":
            for i in range(5):
                print()

            print("WELCOME TO DEPOSIT SECTION")

            username = input("Enter username")
            password = input("Enter password")
            amount = int(input("Enter amount to deposit"))

            output, amt = BANK.deposit(username, password, amount)
            print(output)
            print("AMOUNT IN ACCOUNT = ", amt)

        elif o1.lower() == "b":
            for i in range(5):
                print()

            print("WELCOME TO WITHDRAW SECTION")

            username = input("Enter username")
            password = input("Enter password")
            amount = int(input("Enter amount to withdraw"))

            output, amt = BANK.withdraw(username, password, amount)
            print(output)
            print("AMOUNT IN ACCOUNT = ", amt)

        else:
            for i in range(5):
                print()

            for i in range(5):
                print()
            print("THANK YOU FOR VISITING MY BANK")
            print("PLEASE VISIT AGAIN")
            exit(0)
            break


if __name__ == "__main__":
    main()