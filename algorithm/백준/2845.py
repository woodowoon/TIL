# 브론즈4
# 파티가 끝나고 난 뒤

a, b = map(int, input().split())
temp = list(map(int, input().split()))
temp1 = []
c = a * b

for i in range(len(temp)) :
    temp1.append(temp[i] - c)

print(*temp1)

# 다른사람 풀이1
a, b = map(int, input().split())
people = list(map(int, input().split()))
party = a * b
for i in people:
    print(i - party, end=' ') # 바로 i를 통해 출력하는 방법도 있다.