# 나는 요리사다

sc_list = []
for i in range(5):
    score = map(int, input().split())
    sc_list.append(sum(score))

print(sc_list.index(max(sc_list)) + 1, max(sc_list))