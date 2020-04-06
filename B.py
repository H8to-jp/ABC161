N, M = map(int, input().split())
A = list(map(int, input().split()))

border = sum(A) / (4 * M)
pnum = 0
for i in range(N):
    test = A[i] - border
    if test >= 0:
        pnum +=1
    else:   #test < 0
        pass
    if pnum >= M:
        break
    else:
        pass

if pnum >= M:
    print('Yes')
else: #pnum < M
    print('No')