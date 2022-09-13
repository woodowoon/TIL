# 시험점수

S_score = list(map(int, input().split()))
T_score = list(map(int, input().split()))

S = sum(S_score)
T = sum(T_score)

if (S == T):
    print(S)
else:
    print(max(S, T))