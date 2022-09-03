# 최댓값

nums = []
for i in range(9):
    nums.append(int(input())) # int로 변환해주는 것 매우 중요하다.

print(max(nums))
print(nums.index(max(nums)) + 1)

