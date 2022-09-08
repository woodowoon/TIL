# 핸드폰 요금
# 영식요금제 = 10 * (n // 30) + 10
# 민식요금제 = 15 * (n // 60) + 15

N = int(input())
s = list(map(int, input().split()))

moneyM = 0
moneyY = 0

for i in s:
    moneyY += 10 * (i//30) + 10 # +10을 해주는 이유는 통화를 시작할때부터 10원이 추가되기 때문이다.
    moneyM += 15 * (i//60) + 15

if(moneyY == moneyM) :
    print("Y", "M", moneyM)
elif(moneyY > moneyM) :
    print("M", moneyM)
else:
    print("Y", moneyY)