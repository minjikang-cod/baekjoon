import sys
input = sys.stdin.readlines
sys.setrecursionlimit(10**6)
lines = input()
tree = [[] for _ in range(int(lines[0])+1)]
for l in lines[1:]:
    a, b, c = map(int, l.split())
    tree[a].append([b,c])
    tree[b].append([a,c])
    
def max_length(node, weight):
    for next_node, next_weight in tree[node]: # 현재 노드에서 갈 수 있는 모든 노드들에 대해
        if visited[next_node] == -1: # 방문한 적 없다면
            visited[next_node] = weight+next_weight # 다음 노드까지의 가중치는 현재 가중치에 다음으로 가는 것 합치기
            max_length(next_node, weight+next_weight) # 다음 노드를 기준으로 또 갈 수 있는 모든 노드들 현재 가중치 값 상태에서 점검 

visited = [-1]*(int(lines[0])+1)
visited[0]=1 # 루트노드는 다시 방문하지 않게
max_length(1,0) # 먼저 루트노드에서 가장 먼 노드 찾기
node_a = visited.index(max(visited))

visited = [-1]*(int(lines[0])+1)
visited[node_a]=0 # 첫 노드는 다시 방문하지 않게
max_length(node_a,0) # 위에서 찾은 노드로부터 가장 먼 노드 찾기

print(max(visited))
