# 브론즈5 문제
# 킹, 퀸, 룩, 비숍, 나이트, 폰

answer = [1, 1, 2, 2, 2, 8]
write = list(map(int, input().split()))

for i in range(len(answer)) :
    print(answer[i]-write[i], end=" ")
