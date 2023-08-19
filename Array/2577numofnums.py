#2577
A = int(input())
B = int(input())
C = int(input())

result = A*B*C

str_result = str(result)

for i in range(10):
    print(str_result.count(str(i)))
