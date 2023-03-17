import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())
edge = {i:[] for i in range(1, V+1)}
for _ in range(1, V+1): # 틀리는데 가장 중요한 역할을 한 녀석... 정점에 대한 정보가 순서대로 입력되는게 아니다,,,
    info = list(map(int, input().split()))
    i = info[0]; info = info[1:-1]
    for j in range(len(info)//2):
        edge[i].append((info[j*2], info[j*2+1])) # [연결된 정점, 간선 거리]

def dfs(node, dist):
    visited[node] = dist 
    for next_node, next_dist in edge[node]:
        if visited[next_node] == -1:
            dfs(next_node, dist+next_dist)

answer = 0
visited = [-1]*(V+1)
dfs(1, 0)
point = visited.index(max(visited)) # 임의의 루트에서 가장 먼 노드 구하기

visited = [-1]*(V+1)
dfs(point, 0) # 해당 노드에서 시작해서 거리 구하기
print(max(visited))









'''
            1
         '2'
        3
     '3'
    4
 '4' '6'
2       5



'''