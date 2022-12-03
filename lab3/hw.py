from enum import Enum
import sys
class WalletType(Enum):
    KZT = 'KZT'
    USD = 'USD'
    EUR = 'EUR'
    RUB = 'RUB'




class BankAccount:
    balance = 0

    def __init__(self, name: str, surname: str, account: WalletType) -> None:
        self.name = name
        self.surname = surname
        self.account = account
    
    def __str__(self) -> str:
        return f'{self.name} {self.surname} {self.balance} {self.account}'
    
    
    def __del__(self):
        print('Inside destructor')
        print('Object destroyed')
    
    def addToBankAccount(self, add: int)-> None:
        self.balance += add


    def substractFromBankAccount(self, sub: int) -> None:
        self.balance -= sub
        
    def moneyConversion(self, moneyType: WalletType) -> None:
        if self.account == moneyType:
            print(f'Your balance has already been converted')
            
        elif moneyType == 'USD':
            if self.account == 'EUR':
                self.balance *= 1.05 
            
            elif self.account == 'KZT':
                self.balance *= 0.0021
            
            elif self.account == 'RUB':
                self.balance *= 0.016
            print(f'Your balance converted {self.account} to {moneyType}')           
            self.account = 'USD'
        
        elif moneyType == 'KZT':
            if self.account == 'EUR':
                self.balance *= 495.43 
            
            elif self.account == 'USD':
                self.balance *= 470.16
            
            elif self.account == 'RUB':
                self.balance *= 7.52
            print(f'Your balance converted {self.account} to {moneyType}')           
            self.account = 'KZT'            
            
        elif moneyType == 'RUB':
            if self.account == 'EUR':
                self.balance *= 65.86
            
            elif self.account == 'USD':
                self.balance *= 62.50
            
            elif self.account == 'KZT':
                self.balance *= 0.13
            print(f'Your balance converted {self.account} to {moneyType}')           
            self.account = 'RUB'                        

        elif moneyType == 'EUR':
            if self.account == 'KZT':
                self.balance *= 0.0020 
            
            elif self.account == 'USD':
                self.balance *= 0.95
            
            elif self.account == 'RUB':
                self.balance *= 0.015
            print(f'Your balance converted {self.account} to {moneyType}')           
            self.account = 'EUR'  


# db = []
# cnt = 0

# while True:
#     print('If u want to create bank account type 1 ')
#     print('If u want to select bank account type 2 ')
#     print('if u want to quit main menu type 0 ')
#     command = int(input())
#     if command == 0:
#         sys.exit()
#     elif command == 1:
#         cnt += 1
#         info = input('Please input your data look like this Name Surname WalletType ').split()
#         P1 = BankAccount(info[0], info[1], info[3])
#         db.append(P1)
#         print(f'Your account has been successfully registered your number {cnt} ')

#     elif command == 2:
#         print('If u want to see your balance type "balance" and number ')
#         print('If u want to convert balance type "convert" and number and type currency ')
#         print('If u want to withdraw money type "withdraw" and number and money ')
#         print('if u want to top up your balance type "add" and number and money ')
#         cmd = input().split()
#         if cmd[0] == 'balance':
#             print(db[int(cmd[1])].balance)
#         if cmd[0] == 'convert':
#             print(db[int(cmd[1])].moneyConversion(cmd[3]))
#         if cmd[0] == 'withdraw':
#             print(db[int(cmd[1])].substractFromBankAccount(int(cmd[3])))            
#         if cmd[0] == 'add':
#             print(db[int(cmd[1])].addToBankAccount(int(cmd[3])))