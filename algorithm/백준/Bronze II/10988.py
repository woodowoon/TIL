# 팰린드롬인지 확인하기

word = input()
first_word = word[0:len(word)//2]
if(len(word)% 2 == 1) :
    end_word = word[len(word)//2 +1 :len(word)]
    end_word = end_word[::-1]
else:
    end_word = word[len(word)//2 : len(word)]
    end_word = end_word[::-1]

if(first_word == end_word):
    print(1)
else:
    print(0)

# 다른사람 풀이1
word = list(str(input()))

if list(reversed(word)) == word: # reversed : 반대로 바꿔주는 내장함수
    print(1)
else:
    print(0)

# 다른사람 풀이2
# 와.. 이렇게 짧고 간단하게.. 풀이가 가능하다.
# 1은 if a == a[::-1] 이 같을때 출력하고 else 의 경우 0을 출력해준다.
a = input()
print(1 if a==a[::-1] else 0) # ::-1 을 이용하면 반대로 바꿔줄 수 있다.