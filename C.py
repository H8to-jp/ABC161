N, K = map(int, input().split())

ans = N % K
ans2 = (ans - K) * -1

if ans2 < ans:
    print(ans2)
else:   #ans2 <= ans1
    print(ans)


        

    