import sys
from collections import deque
input = sys.stdin.readline
limit_number = 10**6
sys.setrecursionlimit(limit_number)

def bfs(visit, edge, start):
    queue = deque()
    visit[start] = True
    print(start)
    queue.append(start)
    while queue:
        s = queue.popleft()
        for e in edge[s]:
            if not visit[e]:
                visit[e] = True 
                print(e)
                queue.append(e)

if __name__ == "__main__":
    N, M, R = map(int, input().split())
    edge = dict([(i,[]) for i in range(1,N+1)])
    visit = [False] * (N+1)

    for _ in range(M):
        p1, p2 = map(int, input().split())
        edge[p1].append(p2)
        edge[p2].append(p1) 
    
    for key, value in edge.items():
        edge[key] = sorted(value)
        
    bfs(visit, edge, R)
    for v in range(1, N+1):
        if not visit[v]:
            print(0)