# 지능형 기차

people = []
peo = 0

for i in range(4):
    a, b = map(int, input().split())
    people.append(peo - a + b)
    peo = peo - a + b

print(max(people))

