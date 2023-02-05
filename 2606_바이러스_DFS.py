import sys
input = sys.stdin.readline

node = int(input())
edge = int(input())
network = dict([(i,[]) for i in range(1,node+1)])
visit = [False] * (node+1)

for e in range(edge):
    a, b = map(int, input().split())
    network[a].append(b);network[b].append(a)

stack = [1]; visit[1] = True

while stack:
    last = stack.pop()
    for l in network[last]:
        if not visit[l]:    stack.append(l); visit[l] = True

print(sum(visit[2:]))