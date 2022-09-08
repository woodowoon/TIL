# R2
# s = (R1 + R2) / 2
# R1과 s 이 주어질때, R2를 구하시오.

R1, S = map(int, input().split())
R2 = (2*S) - R1
print(R2)
