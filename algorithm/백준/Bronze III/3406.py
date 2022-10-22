# 이진수

N = int(input())

for i in range(N):
    num = int(input())
    count = 0
    while num > 0:
        if num % 2 == 1:
            print(count, end=' ')
        count += 1
        num = num // 2
