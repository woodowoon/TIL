# 단어공부


a = input().upper()

counts =[]
print(a)

for i in range(len(a)) : # 문제점이 있다. 중복적으로 가장 많은 값이 있을때, ? 가 출력이 되지않는다.
    counts.append(a.count(a[i]))

print(a[counts.index(max(counts))])

# 코드를 찾아보면서 내식으로 바꾸기
word = input().upper()
unique_word = list(set(word)) # set를 이용해서 중복적인 것을 빼준다.
cnt = []

for i in unique_word : # unique_word 를 돌아라
    cnt.append(word.count(i))  # cnt에는 word를 unique_word 별로 word를 카운트 한 값을 넣어라.

if cnt.count(max(cnt)) >= 2: # 중복된 값이 있으면.
    print("?")
else :
    print(unique_word[(cnt.index(max(cnt)))])
