#2309
height_list = [int(input()) for _ in range(9)]
sum_height = sum(height_list)

for i in range(len(height_list)): 
    for j in range(len(height_list)):
        if sum_height - height_list[i] - height_list[j] == 100:
            if height_list[i] != height_list[j]:
                copy_list = height_list[:]
                copy_list.remove(height_list[i])
                copy_list.remove(height_list[j]) 
                copy_list.sort()       

for i in copy_list:
    print(i)


