# OX 퀴즈
# 나중에 다시 한번 풀어보기

n = int(input())

for i in range(n) :
    ox_list = list(input())
    score = 0
    sum = 0
    
    for j in ox_list:
        if j == "O" : # 정답이면
            score += 1
            sum += score
        else :
            score = 0
    print(sum)