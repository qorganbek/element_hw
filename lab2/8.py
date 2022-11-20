class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.exchange_rate = True

    is_usd = False

    def add_money(self, money):
        self.balance += money

    def withdraw_money(self, money):
        self.balance -= money

    def convert_usd_to_kzt(self):
        if self.is_usd:
            self.balance /= 461
            self.is_usd = False

    def convert_kzt_to_usd(self):
        if self.is_usd == False:
            self.balance *= 461
            self.is_usd = True


p1 = Bank(int(input('Your balance! ')))
p1.add_money(int(input('Enter how much you will add! ')))
p1.withdraw_money(int(input('how much money do you want to withdraw! ')))
a = input('If u want to convert balance kzt to usd type "1" ')
if a == '1':
    p1.convert_kzt_to_usd()

print(p1.balance)





