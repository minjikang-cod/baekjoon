from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    sentence = input().split()
    if sentence[0] == 'push':
        queue.append(int(sentence[1]))
        
    elif sentence[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
            
    elif sentence[0] == 'size':
        print(len(queue))
        
    elif sentence[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif sentence[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif sentence[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)        