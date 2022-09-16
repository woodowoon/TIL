# 열개씩 끊어 출력하기
# 슬레이싱 기법 사용하기

s = input()

for i in range(0, len(s), 10):
    print(s[i:i+10])
    