# 네 번째 점

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

x_list = [a[0], b[0], c[0]]
y_list = [a[1], b[1], c[1]]

for i in range(3):
    if(x_list.count(x_list[i]) == 1) :
        x = x_list[i]
    if(y_list.count(y_list[i]) == 1) :
        y = y_list[i]

print(x, y)

