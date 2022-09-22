# 영수증

total_price = int(input())
price = []

for i in range(9):
    price.append(int(input()))

price = sum(price)

print(total_price - price)