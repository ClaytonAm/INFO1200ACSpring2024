from BankAccount import Bank
import random


def main():
    print("Welcome to Kodey's Bank App")
    print()

    accounts = getAccounts()
    showAccounts(accounts)

    choice = 'y'
    while choice.lower() == 'y':
        selected_acct = getAccount(accounts)
        print(selected_acct.applyRandomGift(random.randint(500, 1500)))


def getAccount(accts):
    while True:
        try:
            number = int(input("Enter Account Number: "))
            if number < 1 or number > len(accts):
                print(f"Number must be between 1 and {len(accts)}")
            else:
                return accts[number-1]
        except:
            print("Please enter a valid number.")


def showAccounts(accts):
    print("ACCOUNTS")
    print("--------")
    for i, acc in enumerate(accts, start=1):
        print(f"{i}. {acc.name}")
    print()


def getAccounts():
    return (Bank("Kodey's Checking", 1000, 0.01),
            Bank("Jane's CD", 5000, .08),
            Bank("Marcus MM", 40000, .055))


if __name__ == "__main__":
    main()
