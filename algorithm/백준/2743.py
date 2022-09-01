# 새싹 문제
# 단어 길이 재기

# 처음에는 이렇게 작성하였다. 하지만 런타임 오류로 인해서 다시 생각해보았다.
from asyncio.windows_events import NULL

a = ''
count = 0
a = input()
for i in range(len(a)):
    if (a[i] != NULL):
        count += 1
    else :
        break

print(count)

# 2번째 풀이
a = ''
a = input()
print(len(a))

# 다른 사람의 풀이
# 와 이걸 보고 놀랐다. 이렇게도 풀 수 있구나.
print(len(input()))