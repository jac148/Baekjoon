from itertools import permutations
N = int(input())
num = list(map(int,input().split()))
 
per = permutations(num) #generate all possible permutations of num
sum_max = 0
 
for i in per:
    s = 0
    for j in range(len(i) - 1):
        s += abs(i[j] - i[j+1])
    if s > sum_max:
        sum_max = s

print(sum_max)