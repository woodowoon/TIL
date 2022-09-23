# 나머지

list = []
for i in range(10):
    a = int(input())
    list.append(a % 42)

answer = set(list) # 중복제거
print(len(answer))