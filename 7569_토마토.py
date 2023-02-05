from collections import deque
import sys
input = sys.stdin.readline

N, M, H = map(int,input().split())
tomatoes = []
queue = deque()
count = 0
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

for h in range(H):
    box = []
    for m in range(M):
        T = list(map(int, input().split()))
        box.append(T)
        for t in range(len(T)):
            if T[t]==1:                     # 익은 토마토 자리를 일단 입력받으면서 다 큐에 저장해두기(BFS)
                queue.append([h,m,t])
    tomatoes.append(box)
    
while queue:
    px, py, pz = queue.popleft()
    for k in range(6):
        xx = px+dx[k]
        yy = py+dy[k]
        zz = pz+dz[k]
        if 0 <= xx < H and 0<= yy < M and 0 <= zz < N and tomatoes[xx][yy][zz]==0: # 각 자리 주변에 안 익은 토마토 있으면
            tomatoes[xx][yy][zz] = tomatoes[px][py][pz]+1 # 방문하면서 숫자 갱신해주기
            queue.append([xx,yy,zz])

max_num = 0
for i in tomatoes:
    for j in i:
        for k in j:
            if k==0:
                print(-1); exit(0)
            max_num = max(max_num, k)
print(max_num-1)
            
    
    
    