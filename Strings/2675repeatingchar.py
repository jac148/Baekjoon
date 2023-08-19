#2675
N = int(input())

for _ in range(N):
    times, word = input().split()
    for i in word:
        print(i*int(times), end ='')
    print()