# 거스름돈
# 그리드

money = int(input())
re = 1000 - money
result = 0

money_list = [500, 100, 50, 10, 5, 1]
re_list = []

for i in money_list:
    if re == 0:
        break;
    
    result += re // i
    re %= i

print(result)