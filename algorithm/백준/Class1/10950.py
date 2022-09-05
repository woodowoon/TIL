# A+B - 3

n = int(input())

for i in range(n) :
    a, b = map(int, input().split())
    print(a + b)

# A+B - 4

while True:
    try :
        a, b = map(int, input().split())
        print(a + b)
    except:
        break

# A+B - 5
while True:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break
    
    print(a + b)

    