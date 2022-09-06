# 주사위 세개

nums = list(map(int, input().split()))
cnt = []

for i in nums:
    cnt.append(nums.count(i))

if (max(cnt) == 1) : # 한개도 같지 않을때
    print(max(nums) * 100)
elif (max(cnt) == 2) : # 2개가 같을때
    a = cnt.index(max(cnt))
    print(1000 + nums[a] * 100)
else: # 3개가 같을때
    print(10000 + nums[1] * 1000)
