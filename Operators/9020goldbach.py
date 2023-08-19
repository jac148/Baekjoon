import math
def prime(N):
    if N == 1:
        return False
    for i in range(2,int(math.sqrt(N))+1): #O(N), O(N^2)
        if N % i == 0:
            return False
    return True

T = int(input()) #test case

for _ in range(T):
    num = int(input())  # input even number
    A = num // 2
    for _ in range(num//2+1):
        if prime(A) and prime(num-A):
            print(A, num-A)
            break
        else:
            A -= 1


