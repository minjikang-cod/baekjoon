import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    sentence = input().split()
    if sentence[0] == 'push':
        stack.append(sentence[1])
    elif sentence[0]== 'pop':
        if stack:   print(stack.pop())
        else:       print(-1)
    elif sentence[0]== 'size':
        print(len(stack))
    elif sentence[0]== 'empty':
        if stack:   print(0)
        else:       print(1)
    elif sentence[0]== 'top':
        if stack:   print(stack[-1])
        else:       print(-1)