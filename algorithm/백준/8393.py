# 브론즈5 문제
# 합

a = int(input())
sum = 0
for i in range(1, a+1):
    sum += i

print(sum)

# 다른사람 풀이
print(sum(range(1, int(input())+1))) # 한줄로 나타낼 수 있다.