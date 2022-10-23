# A < B < C

num_list = list(map(int, input().split()))
str_list = input()

num_list.sort()
A = num_list[0]
B = num_list[1]
C = num_list[2]

for i in str_list:
    if(i == 'A'):
        print(A, end=' ')
    elif(i == 'B'):
        print(B, end=' ')
    elif(i=='C'):
        print(C, end=' ')