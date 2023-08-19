N, M = map(int, input().split()) # [10,5]
elementArray = list(map(int,input().split()))

for i in range(N):
    if elementArray[i] < M:
        print(elementArray[i])