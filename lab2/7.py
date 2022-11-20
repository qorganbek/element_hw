s = input()
cnt_t = 0
cnt_f = 0

for i in s:
    if i == '1':
        cnt_t += 1
    elif i == '0':
        cnt_f += 1

if cnt_f > cnt_t:
    print(0)
else:
    print(1)
