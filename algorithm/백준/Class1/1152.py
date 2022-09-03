# 단어의 개수

# 내코드인데 계속.. 틀렸다고 떴다. 아무리 생각해도 이유를 모르겠어서 다른 코드를 보았다.
a = input()
b = a.strip()
count = 0

for i in range(len(b)) :
    if(b[i] == " "):
        count += 1

print(count+1)

# 다른코드1
a = input().split() # 공백마다 입력을 받아서 단어들의 길이를 구해준다.
print(len(a))

# 다른코드2
print(len(input().split()))



