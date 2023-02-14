import sys
from collections import deque
input = sys.stdin.readlines 

cheese = [] # 치즈판
for i in input()[1:]:
    cheese.append(list(map(int,i.split())))
R, C = len(cheese), len(cheese[0]) # row, column
melting = [] # 녹는 치즈
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def BFS(cheese):
    visited = [[0 for _ in range(C)] for _ in range(R)] # 방문여부 확인
    queue = deque([(0,0)]) # 좌측상단(가장자리에 포함됨 → 치즈 없음) 큐에 포함
    visited[0][0] = 1
    m_cnt = 0
    while queue:
        x, y = queue.popleft() 
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i] 
            if 0<=nx<R and 0<=ny<C and not visited[nx][ny]:
                if cheese[nx][ny]==0: # 아직 공기중이라면
                    queue.append((nx,ny))
                else: # 치즈를 만났다면
                    m_cnt += 1 # 녹일 치즈 개수 추가
                    cheese[nx][ny]=0 # 녹았다치고 공기로 바꿔
                visited[nx][ny]=1

    return m_cnt

while True:
    cnt = BFS(cheese)
    if cnt:     melting.append(cnt)
    else:       break 

print(len(melting))
print(melting[-1])