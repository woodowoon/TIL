# 삼각형 외우기
a = int(input())
b = int(input())
c = int(input())

if(sum([a, b, c]) == 180):
    if(a == b == c == 60):
        print("Equilateral")
    elif(a==b or b==c or c==a):
        print("Isosceles")
    else :
        print("Scalene")
else:
    print("Error")