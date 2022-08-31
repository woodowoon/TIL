# 브론즈5
# 행렬덧셈
# 나중에 한번더 볼 것.

# 계속 틀렸다고 뜬다 이유가 뭐지..?
n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split()))) # list 형태로 a에 값을 넣는다.

for i in range(n):
    b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n) :
        a[i][j] += b[i][j]

for i in a:
    print(*i)

# 다른 사람 풀이1
n, m = map(int, input().split())
a, b = [], []
for i in [a, b]: # 한번에 입력받는걸 볼 수 있다.
    for j in range(n):
        i.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]
    print(*a[i])

# 다른 사람 풀이2
# 메모리 효율성을 위해서 temp를 활용해서 입력받고 더하고 해당 값을 저장하고 입력받은 값은 버린다.
n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(list(map(int, input().split()))) 
    
for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(n) :
        board[i][j] += temp[j] 
        
for i in range(n) : 
    for j in range(n) :
        print(board[i][j], end=" ")
    print()

