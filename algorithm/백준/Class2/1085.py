# 직사각형에서 탈출

x, y, w, h = map(int, input().split())
result = []

result.append(x - 0)
result.append(y - 0)
result.append(w - x)
result.append(h - y)

print(min(result))

# 다른사람 풀이
x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y)) # result 를 이용해서 넣지 않아도 이렇게 풀게되면 메모리적으로도 굉장히 좋을 것 같다.
