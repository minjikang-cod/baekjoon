import sys
input = sys.stdin.readlines
from heapq import heappush, heappop

lines = input()
V, E = map(int, lines[0].split())
edges = {i:[] for i in range(1,V+1)}
start = int(lines[1].rstrip())
visited = [-1]*(V+1)
queue = [[0, start]]

for l in lines[2:]:
    u,v,w = map(int, l.split())
    edges[u].append([v,w])

while queue:
    time, vertex = heappop(queue)
    if visited[vertex] == -1:
        visited[vertex] = time
        for n, e in edges[vertex]:
            heappush(queue, [time+e, n])
            
for v in visited[1:]:
    if v == -1:
        print('INF')
    else:
        print(v)