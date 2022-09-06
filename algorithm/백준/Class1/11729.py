# 숫자의 합

n = int(input())
nums = list(map(int, input()))
count = 0
for i in range(len(nums)):
    count += nums[i]
print(count)
