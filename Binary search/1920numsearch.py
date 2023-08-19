N = int(input())
list1 = list(map(int, input().split()))

M = int(input())
list2 = list(map(int, input().split()))
list1.sort()

#binary search
for num in list2:
    lt, rt = 0, N-1
    isExist= False
    
    while lt <= rt:
        mid = (lt+rt) // 2
        if num == list1[mid]:
            isExist = True
            print(1)
            break
        elif num > list1[mid]:
            lt = mid +1
        else:
            rt = mid - 1
    if not isExist:
        print(0)

