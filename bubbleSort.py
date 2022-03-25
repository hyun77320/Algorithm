n = int(input())
cnt = 0;

num_list = list(map(int, input().split()))

if len(num_list) > n:
    print("error")
    exit()
if len(num_list) < n:
    print("error")
    exit()

for i in range(n-1 , 0 , -1):
    swap = False
    for j in range(i):
        if num_list[j] > num_list[j + 1]:
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
            cnt += 1
            swap = True
    if not swap:
        break
print(num_list)
print(cnt)