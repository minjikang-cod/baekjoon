import sys
from collections import deque
input = sys.stdin.readlines

lines = input()[:-1]
N = int(lines[0])
router = deque()
cnt = 0

for l in lines[1:]:
    packet = l.rstrip()
    if packet == '0':
            router.popleft()
    elif len(router) < N:
            router.append(packet)

print(' '.join(router) if router else 'empty')