m, n = list(map(int, input().split()))

def GCD(m, n):
    if m % n == 0:
        return n
    return GCD(n, m % n)

gcd = GCD(m, n)
lcd = m * n / gcd
print(gcd, end='\n')
print(int(lcd))