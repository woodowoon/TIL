# 과자

a, b, c = map(int, input().split())

x = a * b

y = x - c

if(y < 0):
    print(0)
else:
    print(y)