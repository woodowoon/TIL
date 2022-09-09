# 상근날드

B = []
C = []

SB = int(input())
JB = int(input())
HB = int(input())
Cola = int(input())
Cider = int(input())

B.append(SB)
B.append(JB)
B.append(HB)
C.append(Cola)
C.append(Cider)

print(min(B)+min(C) - 50)

# 다른사람 코드
b = 2000 # 2000원 이하라는 조건이있기때문에
c = 2000
for i in range(3):
    temp = int(input())
    b = min(b, temp)
for i in range(2):
    temp = int(input())
    c = min(c, temp)

print(b + c - 50)

