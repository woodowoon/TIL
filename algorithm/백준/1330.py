# 세씩 문제
# 두 수 비교하기
A, B = map(int, input().split())
if (A == B) :
    print("==")
else :
    (print("<") if A < B else print(">"))

# 자바때문에 (x > y) ? "참" : "거짓" 이렇게 하려고했는데 파이썬에서는 지원해주지않는다.