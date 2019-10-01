class Bank_account:
    def __init__(self, Name, Bank, Balance):
        self.Name = Name
        self.Bank = Bank
        self.Balance = self.set_balance(Balance)

    def set_balance(self, Balance):
        if isinstance(Balance, float):
            return Balance
        raise Exception

data = input()

list_of_account = []

while data != 'end':

    Name, Bank, Balance = list(data.split(' | '))
    account = Bank_account(Name, Bank, float(Balance))
    list_of_account.append(account)
    data = input()

def order_account(account):
    ordered_account = sorted(list_of_account, key=lambda obj: (-obj.Balance, len(obj.Bank)))
    return ordered_account

for ac in order_account(list_of_account):
        print(f"{ac.Bank} -> {ac.Balance:.2f} ({ac.Name})")


