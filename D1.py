from collections import deque
K = int(input())

Current = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while 1:
    Next = deque([])
    cnt = len(Current) 
    if K <= cnt:
        #現在の桁の中で考える
        ans = Current[K - 1]
        break
    else:   #K > cnt
        #次の桁を考える
        for i in Current:
            key = i % 10
            for j in [key - 1, key, key + 1]:
                if 0 <= j and j <= 9:
                    Next.append(i * 10 + j)
                else: #j < 0 or 9 < j
                    pass
        K -= cnt
        Current = Next


print(ans)
