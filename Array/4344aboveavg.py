#4344
C = int(input()) # test cases

for _ in range(C):
    grades = list(map(int, input().split()))
    avg = sum(grades[1:])/grades[0]

    count = 0 # to count number of students below average
    for i in grades[1:]:
        if i > avg:
            count += 1
    per = (count/grades[0])*100
    print('%.3f' %per + '%') #소수점 3번째짜리까지만 출력



