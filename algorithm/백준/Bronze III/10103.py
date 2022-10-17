# 주사위 게임

a_score = 100
b_score = 100
N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    if(a > b):
        b_score -= a
    elif(b > a) :
        a_score -= b
    
print(a_score)
print(b_score)