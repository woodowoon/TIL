# 대회 or 인턴

n, m, k = map(int, input().split())
team = 0

while True :
    n -= 2
    m -= 1
    
    if n<0 or m<0 or (n+m)<k: # 나는 바보인게 분명해... m+m < k 해놓고 왜 오류지? 하면서 한참 찾았다..
        break

    team += 1

print(team)