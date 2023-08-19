N = int(input())

words = [str(input()) for i in range(N)]  # create a list to store strings

words = list(set(words)) # remove duplicated words
words.sort()
words.sort(key=len)

for i in words:
    print(i)