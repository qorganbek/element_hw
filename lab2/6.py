def pow(a, n):
    if n == 0:
        return 1
    res = pow(a * a, int(n / 2))
    if n % 2:
        res *= a
    return res



s = input()
a = int(s.split()[0])
n = int(s.split()[1])
print(pow(a, n))
