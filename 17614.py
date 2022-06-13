n = int(input())
cnt = 0

for i in range(1, n+1):
    i_str = str(i)
    cnt += i_str.count("3") + i_str.count("6") + i_str.count("9")

print(cnt)