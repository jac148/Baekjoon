#5568
from itertools import permutations

n = int(input())
k = int(input())

num_list = []
result = set()

for i in range(n):
    num = input()
    num_list.append(num)
for per in permutations(num_list, k):
    result.add(''.join(per))

print(len(result))



