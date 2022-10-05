# 다이얼

number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

input = list(input())
time = 0

for i in input:
    for j in number:
        if i in j :
            time += number.index(j) + 3

print(time) 