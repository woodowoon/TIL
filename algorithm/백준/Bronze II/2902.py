# KMP는 왜 KMP 일까?

S = input()
result_list = []
result_list.append(S[0])

for i in range(len(S)):
    if(S[i] == '-'):
        result_list.append(S[i+1])


print(''.join(result_list))
