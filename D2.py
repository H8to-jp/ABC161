from collections import deque
K = int(input())

Queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in range(K):
    x = Queue[0]
    Queue.popleft()
    oneplace = x % 10

    #(1の位の数)-1を付け加えた数を入れる
    if oneplace == 0: #xの1の位が0
        pass
    else:   #xの1の位が0でない
        enqueue = x * 10 + (oneplace - 1)
        Queue.append(enqueue)
    
    #1の位の数を付け加えた数を入れる
    enqueue = x * 10 + oneplace
    Queue.append(enqueue)

    #(1の位の数)+1を付け加えた数を入れる
    if oneplace == 9:   #xの1の位の数が9
        pass
    else:
        enqueue = x * 10 + (oneplace + 1)
        Queue.append(enqueue)

print(x)