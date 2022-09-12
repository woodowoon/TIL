# 10부제
day = int(input())
car = list(map(int, input().split()))
count = 0

for i in range(len(car)) :
    if(car[i] == day) :
        count += 1

print(count)