T = int(input())

for _ in range(T):
    sample = input()
    result = 0

    temp = 0
    for ele in sample:
        if ele == 'O':
            temp += 1
            result += temp
        else:
            temp = 0
    print(result)