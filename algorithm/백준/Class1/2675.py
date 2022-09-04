# 문자열 반복
# 문제를 잘못이해해서 엄청 헤맸다.

n = int(input()) # 몇번 입력받을지 입력받는다.
for i in range(n): # 반복문
    count, s = input().split() # 문자열 반복숫자와 문자열 입력
    text = ''
    for i in s: # 문자열 중심으로 반복
        text += int(count) * i # list안에 count * 문자열각각하나를 곱한걸 넣어준다
    print(text) # 출력