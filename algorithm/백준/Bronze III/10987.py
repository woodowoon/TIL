# 모음의 개수
s = input()
a_list = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in range(len(s)):
    for j in a_list:
        if(s[i] == j):
            count += 1

print(count)