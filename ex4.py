class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance  #приватный атрибут
        self._transactions = []  #история операций
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(f"Пополнение: +{amount}")
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transactions.append(f"Снятие: -{amount}")
        else:
            print("Недостаточно средств")
    
    @property
    def balance(self):  #геттер для баланса
        return self._balance
    
    def show_history(self):
        print("История операций:")
        for transaction in self._transactions:
            print(transaction)

#Тестирование
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)  #должно вызвать ошибку
print(f"Баланс: {account.balance}")
account.show_history()
