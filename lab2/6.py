def pow(a, n):
    if n == 0:
        return 1
    res = pow(a * a, n // 2)
    if n % 2:
        res *= a
    return res


a = float(input())
n = float(input())
print(pow(a, n))
