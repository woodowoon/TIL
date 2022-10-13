# 상수

a, b = map(str, input().split())

a_list = list(a)
b_list = list(b)

a_list.reverse()
b_list.reverse()

a = "".join(a_list)
b = "".join(b_list)

print(max(a, b))

# 다른사람 풀이
# ::-1 을 이용해서 굉장히 간단하게 풀 수 있다는 사실을 알았다!!
num1, num2 = input().split()
num1 = int(num1[::-1])  # [::-1] : 역순
num2 = int(num2[::-1])

print(max(num1, num2)) 