# 새싹문제
# 개수세기

n = int(input())
m = list(map(int, input().split()))
a = int(input())
count = 0

for i in range(n):
    if(m[i] == a) :
        count += 1
    
print(count)

# 다른사람 코드
# 메모리는 같지만 시간지 4ms 더 빨랐다.
N = int(input()) 
N_list = list(map(int, input().split()))
v = int(input()) 
print(N_list.count(v)) # count 함수도 있구나