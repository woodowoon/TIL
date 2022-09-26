# 점수계산

n = int(input())
k = list(map(int, input().split()))
score = 0
count = 0

for i in range(n):
    if(k[i] == 1) :
        score += 1
        
    else :
        score = 0
    
    count += score

print(count)