# 완전 제곱수
# T = int(i ** 0.5) ** 2

M = int(input())
N = int(input())
result_list = []

for i in range(M, N+1) :
    num = int(i ** 0.5) ** 2
    if (i == num) :
        result_list.append(i)

if(len(result_list) <= 0):
    print(-1)
else:
    print(sum(result_list))
    print(min(result_list))
