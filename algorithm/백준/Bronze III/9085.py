# 더하기

T = int(input())

for i in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    print(sum(N_list))