# 알파벳 개수
# 다른사람 풀이, 나중에 다시 한번 더 풀어볼것.

s = input()
cnt = [0] * 26

for i in s:
    cnt[ord(i) - 97] += 1 # 만약 a가 있다면, cnt[0] 에 += 1 을 하라는 뜻

print(*cnt)
