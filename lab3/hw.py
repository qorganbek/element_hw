from enum import Enum
import sys

#enum
class WalletType(Enum):
    KZT = 'KZT'
    USD = 'USD'
    EUR = 'EUR'
    RUB = 'RUB'

#BankAccount
class BankAccount:
    balance = 0
    #constructor function
    def __init__(self, name: str, surname: str, account: WalletType):
        self.name = name
        self.surname = surname
        self.account = account
    
    #toString method
    def __str__(self):
        return f'{self.name} {self.surname} {self.balance} {self.account}'
    
    #destructor function
    def __del__(self):
        # print('Inside destructor')
        print('Object destroyed')
    
    #addToBank Function
    def addToBankAccount(self, add: int):
        self.balance += add

    #widthraw money function
    def substractFromBankAccount(self, sub: int):
        if self.balance == 0:
            print('Error 404')
            return;
        self.balance -= sub
    #money convertor function    
    def moneyConversion(self, moneyType: WalletType):
        if self.account == moneyType:
            print(f'Your balance has already been converted')
            print('-'*43)
            
        elif moneyType == 'USD':
            if self.account == 'EUR':
                self.balance *= 1.05 
            
            elif self.account == 'KZT':
                self.balance *= 0.0021
            
            elif self.account == 'RUB':
                self.balance *= 0.016
            print(f'Your balance converted {self.account} to {moneyType}')
            print('-'*43)           
            self.account = 'USD'
        
        elif moneyType == 'KZT':
            if self.account == 'EUR':
                self.balance *= 495.43 
            
            elif self.account == 'USD':
                self.balance *= 470.16
            
            elif self.account == 'RUB':
                self.balance *= 7.52
            print(f'Your balance converted {self.account} to {moneyType}')
            print('-'*43)           
            self.account = 'KZT'            
            
        elif moneyType == 'RUB':
            if self.account == 'EUR':
                self.balance *= 65.86
            
            elif self.account == 'USD':
                self.balance *= 62.50
            
            elif self.account == 'KZT':
                self.balance *= 0.13
            print(f'Your balance converted {self.account} to {moneyType}')
            print('-'*43)           
            self.account = 'RUB'                        

        elif moneyType == 'EUR':
            if self.account == 'KZT':
                self.balance *= 0.0020 
            
            elif self.account == 'USD':
                self.balance *= 0.95
            
            elif self.account == 'RUB':
                self.balance *= 0.015
            print(f'Your balance converted {self.account} to {moneyType}')
            print('-'*43)           
            self.account = 'EUR'  

#database
db = []
#id
cnt = 0

while True:
    print('Hello!')
    print('If u want to create bank account type 1 ')
    print('If u want to select bank account type 2 ')
    print('if u want to quit main menu type 0 ')
    print('-'*43)
    command = int(input())
    if command == 0:
        print("bye!")
        sys.exit()
    elif command == 1:
        cnt += 1
        info = input('Please input your data look like this Name Surname WalletType ')
        print('-'*43)
        P1 = BankAccount(info.split()[0], info.split()[1], info.split()[2])
        db.append(P1)
        print(f'Your account has been successfully registered your number {cnt} ')
        print('-'*43)
    elif command == 2:
        if len(db) == 0:
            print('No registered account')
            continue
        print('If u want to see your balance type "balance" and number ')
        print('If u want to convert balance type "convert" and number and type currency ')
        print('If u want to withdraw money type "withdraw" and number and money ')
        print('if u want to top up your balance type "add" and number and money ')
        print('if u want to see info for u account type "info"  and your number ')
        print('-'*43)
        cmd = input().split()
        if cmd[0] == 'balance':
            print(f'{db[int(cmd[1])-1].balance} {db[int(cmd[1])-1].account}')
        elif cmd[0] == 'convert':
            print(db[int(cmd[1])-1].moneyConversion(cmd[2]))
        elif cmd[0] == 'withdraw':
            print(db[int(cmd[1])-1].substractFromBankAccount(int(cmd[2])))            
        elif cmd[0] == 'add':
            print(db[int(cmd[1])-1].addToBankAccount(int(cmd[2])))
        elif cmd[0] == 'info':
            print(db[int(cmd[1])-1])    
        else: print('Invalid command')
        print('-'*43)    
    else: print('Invalid command')
    print('-'*43)
            