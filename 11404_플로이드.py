# 플로이드 와샬 : 모든 정점에서 모든 정점으로의 최소거리 측정하기(다익스트라처럼 edge에 비용이 존재)
# 직접 가는 길과 다른 버텍스를 거쳐 가는 길 모두 고려해서 가장 최단 거리를 기록

import sys
input = sys.stdin.readline 

n = int(input())
m = int(input())
min_cost = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    # 같은 경로에 대해 다른 cost를 가지는 입력이 주어질 수 있으니 min을 항상 이용해야해
    min_cost[a][b]=min(min_cost[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j:
                min_cost[i][j] = 0
            else:
                min_cost[i][j] = min(min_cost[i][j], min_cost[i][k] + min_cost[k][j])
            
for c_row in min_cost[1:]:
    for c_col in c_row[1:]:
        print(0 if c_col == sys.maxsize else c_col, end = ' ')
    print()