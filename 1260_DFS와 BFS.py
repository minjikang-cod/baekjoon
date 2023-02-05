import sys
from collections import deque
input = sys.stdin.readline

def depthfirst(visit, dfs, edge, start):
    if not visit[start]:
        visit[start] = True
        dfs.append(start)
    edge[start].sort()
    for e in edge[start]:
        if not visit[e]: depthfirst(visit, dfs, edge, e)
 
def breadthfirst(visit, bfs, edge, start):
    queue = deque([start]); visit[start] =True
    while queue:
        first = queue.popleft()
        bfs.append(first)
        for l in edge[first]:
            if not visit[l]:    queue.append(l); visit[l] = True
        
   
if __name__ == "__main__":
    node, edge, V = map(int, input().split())
    network = dict([(i,[]) for i in range(1,node+1)])
    dfs, bfs = [], []

    for e in range(edge):
        a, b = map(int, input().split())
        network[a].append(b);network[b].append(a)
    
    visit = [False] * (node+1)
    depthfirst(visit, dfs, network, V)
    visit = [False] * (node+1)
    breadthfirst(visit, bfs, network, V)
            
    for d in dfs:
        print(d, end=' ')
    print()
    for b in bfs:
        print(b, end=' ')
    
