# 직각삼각형

# 이렇게 풀었는데, 알고보니 max를 구해서 넣어줘야 했다. C가 꼭 max 이라는 법은 없기 때문이다.
# while True:
#     a, b, c = map(int, input().split())
#     if a == 0 and b == 0 and c == 0 :
#         break
    
#     if (a**2 + b**2 == c**2) :
#         print("right")
#     else:
#         print("wrong")

# 다시풀이
while True:
    a = list(map(int, input().split()))
    max_num = max(a)
    if(sum(a) == 0) : # 리스트의 합구하기
        break
    
    a.remove(max_num)
    
    if(a[0]**2 + a[1]**2 == max_num**2) :
        print("right")
    else:
        print("wrong")