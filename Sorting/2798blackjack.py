N, M = map(int, input().split())

numbers = list(map(int, input().split()))
sum_list = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_num = numbers[i] + numbers[j] + numbers[k]
            if sum_num <= M:
                sum_list.append(sum_num)
print(max(sum_list))


