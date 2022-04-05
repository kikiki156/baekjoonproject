# again
M, N = map(int, input().split())
ary = []
minary = []

for _ in range(M):
    ary.append(input())

for i in range(M-7):
    for j in range(N-7):
        idx1 = 0
        idx2 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if ary[k][l] != 'W':
                        idx1 += 1
                    if ary[k][l] != 'B':
                        idx2 += 1
                elif (k+l) % 2 == 1:
                    if ary[k][l] != 'W':
                        idx2 += 1
                    if ary[k][l] != 'B':
                        idx1 += 1
        minary.append(idx1)
        minary.append(idx2)
print(min(minary))
