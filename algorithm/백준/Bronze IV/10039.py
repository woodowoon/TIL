# 평균 점수
# 5명의 성적이 주어지고, 40점 이하는 40점이라고 생각한다. 
# 이 5명의 평균을 구하시오

sum = 0

for i in range(5):
    sc = int(input())
    if(sc < 40):
        sc = 40
    sum += sc

print(sum // 5)   

