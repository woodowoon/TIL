# 사과

N = int(input())
apple_list = []

for i in range(N):
    student, apple = map(int, input().split())
    apple_list.append(apple % student)

print(sum(apple_list))