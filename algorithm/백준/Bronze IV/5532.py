# 방학숙제
import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

a1 = A // C
a2 = A % C
if(a2 != 0):
    a1 += 1

b1 = B // D
b2 = B % D
if(b2 != 0):
    b1 += 1

print(L - max(a1, b1))

# 다른사람코드
# 메모리적으로 훨씬 더 단축할 수 있다.
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

print(L - max(math.ceil(A/C), math.ceil(B/D))) # math 를 이용해서 좀 더 간결하게 코드를 작성할 수 있다.
# math.ceil 올림해서 정수를 반환해준다.