# 수 정렬하기

N = int(input())
list = []
for i in range(N):
    list.append(int(input()))
    list.sort(reverse=False)

print(*list, sep="\n")