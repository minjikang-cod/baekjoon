import sys
input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    sentence = input().split()
    if sentence[0] == 'push':
        queue.append(sentence[1])

    elif sentence[0] == 'pop':
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print(-1)

    elif sentence[0] == 'size':
        print(len(queue))

    elif sentence[0] == 'empty':
        if len(queue) != 0:
            print(0)
        else:
            print(1)

    elif sentence[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)

    elif sentence[0] == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)