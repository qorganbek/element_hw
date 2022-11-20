x = input()

s = 0
x = x[::-1]
for i in range(len(x)):
    # print(x[i])
    if x[i] == '1':
        s += 2**i



print(s)
