num = int(input())
ary = []
for _ in range(num):
    a = input()
    if a in ary:
        continue
    ary.append(a)
ary.sort()
ary.sort(key=len)
for i in ary:
    print(i)
