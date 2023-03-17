import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline 

N, R, Q = map(int, input().split()) # 정점의 수, 루트 번호, 쿼리의 수
edge = {i:[] for i in range(1, N+1)}
for _ in range(N-1): # 트리는 무조건 사이클 없이 모든 정점이 연결되어 있어야 하므로 N-1개의 간선을 가진다.
    a, b = map(int, input().split())
    edge[a].append(b); edge[b].append(a)
subtree = [0]*(N+1)

def dfs(root):
    subtree[root] = 1 # 자기 자신부터 포함시키기
    for n in edge[root]:
        if not subtree[n]: # 방문한 적 없다면 해당 노드의 자식인 것
            dfs(n)
            subtree[root] += subtree[n]

dfs(R) 
for _ in range(Q):
    print(subtree[int(input())])
            
