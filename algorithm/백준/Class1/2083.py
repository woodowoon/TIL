# 브론즈4 문제
# 럭비클럽

while True:
    name, age, weight = input().split()
    age, weight = int(age), int(weight)

    if name == '#' and age == 0 and weight == 0: # and 를 &으로하면 런타임 오류가 뜬다.
        break

    if age > 17 or weight >= 80:
        print("%s Senior" % name)
    else:
        print("%s Junior" % name)