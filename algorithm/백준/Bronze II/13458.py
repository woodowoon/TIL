# 시험 감독

N = int(input())
people_list = list(map(int, input().split()))
a, b = map(int, input().split())
result_list = []

for i in range(N):
    count = 0
    people_list[i] -= a
    count+=1
    
    if(people_list[i] > 0): 
        if(people_list[i] % b == 0):
            count += (people_list[i] // b)
        else:
            count += (people_list[i] // b) + 1

    result_list.append(count)

print(sum(result_list))
