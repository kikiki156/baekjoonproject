num = int(input())
ary = []
for _ in range(num):
    ary.append(input())
ary.sort()
ary.sort(key=len)
for i in range(num):
    print(ary[i])