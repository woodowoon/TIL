# 분산처리

# 처음에 이런식으로 풀었는데 시간초과가 나왔다.
N = int(input())
for i in range(N):
    result = ''
    a, b = map(int, input().split())
    result = str(a ** b)
    print(result.strip()[-1])

# 다른사람 코드
# 시간초과가 나서 막막해서 확인해보았다.
# 0 ~ 9 까지 제곱했을때 나오는 끝자리가 정해져있었고 해당 패턴에 따라서 풀어주면 되는 문제였다.
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a = a % 10
    
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b = b % 4
        if b == 0:
            print((a**4) % 10 % 10 % 10)
        else:
            print((a**b) % 10 % 10 % 10)