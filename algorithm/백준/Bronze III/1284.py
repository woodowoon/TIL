# 집주소

while True:
    n = 2
    a = int(input())
    if(a == 0):
        break
    n += (len(str(a))-1)
    for i in str(a):
        if(int(i) == 1):
            n += 2
        elif(int(i) == 0):
            n+=4
        else:
            n+=3
    print(n)

