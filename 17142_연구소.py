import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

virus_cd = [] # 바이러스를 놓을 수 있는 장소
board = [] # 연구소
wall_cnt = 0 # 연구소 내 벽 개수
for i in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)
    for j in range(N):
        if temp[j] == 2:
            virus_cd.append((i, j))
        if temp[j] == 1:
            wall_cnt += 1
            
ans_time = sys.maxsize
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

virus_combi = list(combinations(virus_cd, M)) # 바이러스 놓을 자리 조합으로 경우의 수 먼저 세기

def bfs(combi):
    queue = deque()
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    v_time = 0
    for x, y in combi:
        queue.append((x,y))
        visited[x][y] = 0 # 활성 바이러스 있는 곳 처음 표시
    
    while queue:
        x, y = queue.popleft() 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0 and visited[nx][ny] == -1: # 아직 방문하지 않은 빈칸
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    v_time = max(v_time, visited[nx][ny])
                elif board[nx][ny] == 2 and visited[nx][ny] == -1: # 비활성화 바이러스
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1 # 시간 측정에는 안 쓰여
    
    if sum(visited, []).count(-1) != wall_cnt: # 벽보다 -1이 많으면(지나지 않은 빈칸이 있음)
        return sys.maxsize
    return v_time        


for combi in virus_combi:
    ans_time = min(ans_time, bfs(combi))
    
print(ans_time if ans_time != sys.maxsize else -1)
            