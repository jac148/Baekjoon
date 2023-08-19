N = int(input())
numbers = map(int, input().split())
count = 0

for num in numbers:
    if num > 1:
        for i in range(2, num+1):
            if num == i:
                count += 1
                break

            if num % i == 0:
                break



print(count)
