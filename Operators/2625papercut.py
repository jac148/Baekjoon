w, h = list(map(int, input().split()))
n = int(input())
width = [0,w] #positions of vertical cuts
height = [0,h] #positions of horizontal cuts

for _ in range(n):
    a, b = list(map(int, input().split()))
    if a == 0:  #가로 cut
        height.append(b)
    elif a == 1:  #새로 cut
        width.append(b)

width.sort()
height.sort()
result = 0

for i in range(len(width) - 1): 
    for j in range(len(height) - 1):
        x = width[i+1] - width[i] # width of current rectangle
        y = height[j+1] - height[j] #height of current rectangle
        result = max(result,x*y)  
print(result)