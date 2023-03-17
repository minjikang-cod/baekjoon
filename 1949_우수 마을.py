# tree + dp

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline 

N = int(input())
members = [0] + list(map(int, input().split()))
village = {i:[] for i in range(1, N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    village[a].append(b); village[b].append(a)

# 해당 마을이 우수마을에 선정되는지 아닌지를 나눠서 생각해야해
# tree 이므로 방문여부도 check
visited = [0]*(N+1)
dp = [[0,members[i]] for i in range(N+1)] # 0: 우수마을 아니야 / 1: 우수마을이야

def dfs(start): # 1번 마을을 start로 지정
    visited[start] = 1
    
    for v in village[start]:
        if not visited[v]: # 방문한 적 없는 node라면
            dfs(v) # 다음 노드에 대하여 동작하기! 
            dp[start][0] += max(dp[v][0], dp[v][1]) # 우수마을이 아니라면 옆마을의 우수마을 여부 경우 다 비교해서 최댓값으로 더하기
            dp[start][1] += dp[v][0] # 현재 우수마을이라면 옆 동네는 무조건 우수마을 아니여야해

dfs(1)
print(max(dp[1][0], dp[1][1])) # 모든 마을의 경우의 수를 거친 후에 비로소 마지막에 시작점에 최종 max 값이 축적되니까







'''
       1
            2
        3       6
    4               7
5

1 안돼
2 3000          안돼
3 6 안돼         3 4000    6 안돼      3 안돼 6 2000      3 4000 6 2000





'''