T = int(input())

def fa(a):
    num = 1
    for i in range(1, a+1):
        num *= i
    return num

li = []

for i in range(T):
    n, m = map(int, input().split())
    li.append(fa(m) // (fa(n) * fa(m-n)))

print(*li, sep='\n')
