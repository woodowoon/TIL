# 새싹 문제
# 과제 안 내신분..?
temp = [i+1 for i in range(30)]

for i in range(28):
    a = int(input())
    temp.remove(a)

temp.sort()

for i in range(len(temp)):
    print(temp[i])

# 다른 사람 풀이
temp = [i+1 for i in range(30)]

for i in range(28):
    a = int(input())
    temp.remove(a)

# 나는 sort와 for 반복문을 통해서 출력해주었는데 다른 사람은 min, max를 이용해서 출력하였다.
print(min(temp))
print(max(temp))
