a = int(input())
b = int(input())
c = int(input())

if a == b and b == c and c == a:
    print(3)
elif a != b and b != c and a != c:
    print(0)
else: print(2)
