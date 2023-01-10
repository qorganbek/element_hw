import os

os.chdir('C:/')

base_path = os.getcwd()


def ls():
    print(os.listdir())


def cd(path: str):
    os.chdir(path)


def mkdir(name: str):
    os.mkdir(name)


def rmdir(name: str):
    os.rmdir(name)


def make_file(name: str):
    with open(name, 'a') as file:
        file.write('')


def rm_file(name: str):
    os.remove(name)


def read_file(name: str) -> None:
    with open(name, 'r') as file:
        data = file.read()
        for i in data:
            print(i, end='')


def cd(path: str):
    os.chdir(path)


'''
Instructor 
1)If u want to change directory u need to write command cd after that show your path
2)If u want to show all files in this directory write command ls
3)If u want to create file write command mkdir or make_file and with space write name of the file
4)If u want to remove file write command rmdir or rm_file and with space write name of the file
5)If u want to read to file write command read  
'''

print('This terminal created by Dima V1.0')
while True:
    command = input().split()
    if command[0] == 'exit':
        break
    elif command[0] == 'ls':
        ls()
    elif command[0] == 'mkdir':
        mkdir(command[1])
    elif command[0] == 'rmdir':
        rmdir(command[1])
    elif command[0] == 'make_file':
        if os.getcwd() == base_path:
            continue
        make_file(command[1])
    elif command[0] == 'rm_file':
        if os.getcwd() == base_path:
            continue
        rm_file(command[1])
    elif command[0] == 'read':
        read_file(command[1])
    elif command[0] == 'cd':
        cd(command[1])
