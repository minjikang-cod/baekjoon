from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
deq = deque()

for _ in range(N):
    sentence = input().split()
    if sentence[0] == 'push_front':
        deq.appendleft(int(sentence[1]))
    elif sentence[0] == 'push_back':
        deq.append(int(sentence[1]))
    elif sentence[0] == 'pop_front':
        if deq: print(deq.popleft())
        else:   print(-1)
    elif sentence[0] == 'pop_back':
        if deq: print(deq.pop())
        else:   print(-1)
    elif sentence[0] == 'size':
        print(len(deq))
    elif sentence[0] == 'empty':
        if deq: print(0)
        else:   print(1)
    elif sentence[0] == 'front':
        if deq: print(deq[0])
        else:   print(-1)
    elif sentence[0] == 'back':
        if deq: print(deq[-1])
        else:   print(-1)