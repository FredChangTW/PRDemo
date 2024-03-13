from datetime import datetime





class BankAccount:
    s_accountNumberSeed = 1234567890
    instanceCount = 0
    a = 0

    @staticmethod
    def get_instance_count():
        return BankAccount.instanceCount

    def __init__(self, name, initial_balance):
        self.number = str(BankAccount.s_accountNumberSeed)
        BankAccount.s_accountNumberSeed += 1
        self.owner = name
        self._all_transactions = []
        self.make_deposit(initial_balance, datetime.now(), "Initial balance")
        BankAccount.instanceCount += 1

    @property
    def balance(self):
        balance = 0
        for item in self._all_transactions:
            balance += item['amount']
        return balance

    def make_deposit(self, amount, date, note):
        if amount <= 0:
            raise ValueError("Amount of deposit must be positive")
        deposit = {'amount': amount, 'date': date, 'note': note}
        self._all_transactions.append(deposit)

    def make_withdrawal(self, amount, date, note):
        if amount <= 0:
            raise ValueError("Amount of withdrawal must be positive")
        if self.balance - amount < 0:
            raise ValueError("Not sufficient funds for this withdrawal")
        withdrawal = {'amount': -amount, 'date': date, 'note': note}
        self._all_transactions.append(withdrawal)

    def get_account_history(self):
        report = []
        balance = 0
        report.append("Date\t\tAmount\tBalance\tNote")
        for item in self._all_transactions:
            balance += item['amount']
            report.append(f"{item['date'].strftime('%Y-%m-%d')}\t{item['amount']}\t{balance}\t{item['note']}")
        return '\n'.join(report)


class Transaction:
    def __init__(self, amount, date, note):
        self.amount = amount
        self.date = date
        self.note = note


if __name__ == "__main__":
    account = BankAccount("<name>", 1000)
    print(f"Account {account.number} was created for {account.owner} with {account.balance} initial balance.")

    account.make_withdrawal(500, datetime.now(), "Rent payment")
    print(account.balance)
    account.make_deposit(100, datetime.now(), "Friend paid me back")
    print(account.balance)

    try:
        account.make_withdrawal(750, datetime.now(), "Attempt to overdraw")
    except ValueError as e:
        print("Exception caught trying to overdraw")
        print(e)

    print(account.get_account_history())
    print(BankAccount.get_instance_count())
