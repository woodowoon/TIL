# 8진수 2진수

n = input()
a = int(n, 8) # 8진수 -> 10진수로 변환
print(bin(a)[2:]) # bin : 2진수로 변환. 슬라이싱
