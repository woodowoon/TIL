# 공
n = int(input())
cup = [1,2,3]

for _ in range(n):
    n1, n2 = map(int, input().split())
    
    x1 = cup.index(n1)
    y1 = cup.index(n2)

    cup[x1], cup[y1] = cup[y1], cup[x1]

print(cup[0])
