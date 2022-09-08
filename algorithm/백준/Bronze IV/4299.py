# AFC 윔블던
# 경기의 합과 차가 주어지며 이것을 통해서 경기의 점수를 구해라 
# 큰 득점을 구하고 만약 동점이면 -1 출력

# 다른 코드
# 내코드가 오류가 났다..
s, m = map(int, input().split())
if  s+m < 0 or s-m < 0 or (s + m) % 2:
    print(-1)
else:
    a = (s + m) // 2
    b = s - a
    print(max(a, b), min(a, b))