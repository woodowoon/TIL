# 주사위

N = int(input())
result_list = []

for i in range(N):
    a, b, c = map(int, input().split())
    if(a == b == c):
        result_list.append(10000 + a * 1000)
    elif(a == b):
        result_list.append(1000 + a * 100)
    elif(b == c):
        result_list.append(1000 + b * 100)
    elif(a == c):
        result_list.append(1000 + a * 100)
    else:
        max_num = max(a, b, c)
        result_list.append(max_num * 100)

print(max(result_list))