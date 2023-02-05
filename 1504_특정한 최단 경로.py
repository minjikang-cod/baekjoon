import sys
input = sys.stdin.readlines
from heapq import heappush, heappop

lines = input()
N, E = map(int, lines[0].split())
edges = {i:[] for i in range(1,N+1)}

for l in lines[1:E+1]:
    a, b, c = map(int, l.split())
    edges[a].append([b,c])
    edges[b].append([a,c])

def bfs(start, end):
    queue = [[0, start]]
    visited = [-1]*(N+1)
    while queue:
        time, now = heappop(queue)
        if visited[now]== -1:
            if now == end:
                return time
            visited[now] = time
            for n, e in edges[now]:
                heappush(queue, [e+time, n])
    
    return -1

mid_a, mid_b = map(int, lines[E+1].split())
s_ma = bfs(1, mid_a)
s_mb = bfs(1, mid_b)
e_ma = bfs(N, mid_a)
e_mb = bfs(N, mid_b)
mida_b = bfs(mid_a, mid_b)
 
case_a = -1
case_b = -1

if s_ma != -1 and e_mb != -1:
    case_a = s_ma + e_mb
if s_mb != -1 and e_ma != -1:
    case_b = s_mb + e_ma

if case_a == -1 or case_b == -1:
    print(-1)
else:
    print(mida_b + min(case_a, case_b))