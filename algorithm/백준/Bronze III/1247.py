# 부호
# 문제가 이해가 되지 않아요.. -> 이해완료!
# 3개를 테스트 할 것 인데, 맨 처음에 N을 입력받고 N개의 정수를 입력받는다.
# 그리고 이 값들을 전부 더해서 0 - + 부호를 정해주고 또 다시 N을 입력받고 N개의 정수를 입력 받는다.

# 시간초과가 나왔다.
from sys import stdin


for _ in range(3):
    N = int(input())
    nums = []
    for i in range(N) :
        nums.append(int(input()))
    
    if sum(nums) == 0 :
        print("0")
    elif sum(nums) > 0 :
        print("+")
    else :
        print("-")

# 시간초과문제로 stdin.readline 사용!
for _ in range(3):
    N = int(stdin.readline())
    nums = []
    for i in range(N) : # nums = [int(stdin.readline()) for i in range(N)]  다른사람코드인데, nums 에 넣을때 3줄을 1줄로 요약할 수도있을 것 같다. 기능은 같다.
        nums.append(int(stdin.readline()))
    
    if sum(nums) == 0 :
        print("0")
    elif sum(nums) > 0 :
        print("+")
    else :
        print("-")