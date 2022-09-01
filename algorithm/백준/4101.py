# 브론즈 5 문제
# 크냐 ?

while True:
    a, b = map(int, input().split())
    if (a == 0 & b == 0):
        break
    elif (a > b):
        print("Yes")
    else :
        print("No")

# 다른 풀이를 참고하여 내 풀이 수정하기
# 근데 뭐가 더 효율적인지는 모르겠음..
a, b = map(int, input().split())
while not (a == 0 and b == 0): # while 문에 break문을 넣어줘도 된다.
    if a > b :
        print("Yes")
    else :
        print("NO")
    a, b = map(int, input().split())    
    
# 다른사람 풀이 2
while True:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    print("Yes" if a > b else "No") # 삼항연산자 사용


