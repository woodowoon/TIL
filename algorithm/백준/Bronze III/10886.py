# 0 = not cute / 1 = cute

n = int(input())
cute = []

for i in range(n):
    a = int(input())
    cute.append(a)

if(sum(cute) > (n // 2)):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")