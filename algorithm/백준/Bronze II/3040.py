# 백설 공주와 7난쟁이

from itertools import combinations

n = []
for i in range(9):
    n.append(int(input()))

answer = []

for i in combinations(n, 7):
    if(sum(i) == 100) :
        answer.append(i)

result_list = list(answer[0])
print(*result_list, sep="\n")