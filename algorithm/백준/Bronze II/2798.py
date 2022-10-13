# 블랙잭
# 순열 & 조합 문제 이건 조합으로 풀 수 있는 문제인 듯 싶다.
# itertools 를 활용해서 굉장히 쉽게 풀기는 했는데 뭔가 이렇게 말고 정석대로 풀고싶다.
# 나는 순열과 조합의 로직을 잘 모르니깐.. 조금 아쉽긴 하다.

import itertools

N, M = map(int, input().split())
number_list = list(map(int, input().split()))
sum_list = []

data = itertools.combinations(number_list, 3)

for i in data:
    if (sum(i) <= M) :
        sum_list.append(sum(i))

print(max(sum_list))