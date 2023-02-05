import sys
from collections import deque
input = sys.stdin.readline

node = int(input())
edge = int(input())
network = dict([(i,[]) for i in range(1,node+1)])
visit = [False] * (node+1)

for e in range(edge):
    a, b = map(int, input().split())
    network[a].append(b);network[b].append(a)

queue = deque([1]); visit[1] = True

while queue:
    first = queue.popleft()
    for l in network[first]:
        if not visit[l]:    queue.append(l); visit[l] = True

print(sum(visit[2:]))