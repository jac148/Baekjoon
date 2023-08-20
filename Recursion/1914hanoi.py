def hanoi(n, start, end):
    if n == 1:
        print(start, end) #move disk 1 from start to end
        return
    
    hanoi(n-1, start, 6-start-end ) # moving (n-1)disks from start to middle using end as an auxiliary
    print(start, end)  #'n'th disk is moved from start to end
    hanoi(n-1, 6-start-end, end) #move the (n-1)disks from middle to end, using start as an auxiliaty

n = int(input())
print(2**n-1)  
if n <= 20:
    hanoi(n, 1, 3 ) # peg 1 and 3 as the start and end peg

