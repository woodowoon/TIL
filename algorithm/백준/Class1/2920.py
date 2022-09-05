n = list(map(int, input().split()))

if n == sorted(n) :
    print("ascending")
elif n == sorted(n, reverse=True): # sorted reverse=True 는 역방향으로 sort 라는 뜻.
    print("descending")
else :
    print("mixed")
