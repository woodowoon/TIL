# 숫자의 개수

A = int(input()) 
B = int(input())
C = int(input())

answer = str(A * B * C)
answer_list = list(answer)

for i in range(10):
    print(answer_list.count(str(i))) # 애시당초 str 이기때문에 str(i) 라고 해줘야한다.