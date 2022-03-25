num_list = list(map(int, input().split()))

for end in range(1, len(num_list)):
    for i in range(end, 0, -1):
        if num_list[i - 1] > num_list[i]:
            num_list[i - 1], num_list[i] = num_list[i], num_list[i - 1]

for i in range(len(num_list)):
    a = num_list[i]
    print(a, end=' ')