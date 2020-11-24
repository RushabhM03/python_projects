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
            return "WITHDRAWN SUCCESSFULLY"

        else:
            return "INVALID ACCOUNT"

    def deposit(self, username, password, amount):
        account = self.get_account(username, password)

        if account == False:
            return "INVALID CREDENTIALS"

        if amount > 0:
            account.amount += amount
            return "DEPOSIT SUCCESSFULLY"

        else:
            return "INVALID ACCOUNT"


def main():

    print("\t\t\t WELCOME TO MY BANK")
    for i in range(10):
        print()

    BANK = BankSystem()

    username = input("Enter username")
    password = input("Enter password")
    amount = int(input("Enter amount"))

    output = BANK.create_account(username, password, amount)
    print(output)

    username = input("Enter username")
    password = input("Enter password")
    amount = int(input("Enter amount to deposit"))

    output = BANK.deposit(username, password, amount)
    print(output)

    username = input("Enter username")
    password = input("Enter password")
    amount = int(input("Enter amount to withdraw"))

    output = BANK.withdraw(username, password, amount)
    print(output)


if __name__ == "__main__":
    main()