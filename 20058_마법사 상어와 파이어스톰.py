import sys 
from collections import deque
input = sys.stdin.readline 

N, Q = map(int, input().split())
size = 2**N
ice = []
for _ in range(size):
    ice.append(list(map(int, input().split())))
L_list = list(map(int, input().split()))
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def ice_rotate(ice, L): # 얼음판 회전시키기
    new_ice = [[0 for _ in range(size)] for _ in range(size)] # 새 얼음판
    l_size = 2**L
    # 격자 한 칸 마다
    for i in range(0, size, l_size): 
        for j in range(0, size, l_size):
            # 격자 내에서 
            for r in range(l_size):
                for c in range(l_size):
                    new_ice[i+c][j+l_size-r-1] = ice[i+r][j+c]
    
    return new_ice

def ice_melting(ice): # 주변 확인하고 조건에 맞게 얼음 녹이기
    melting_list = []
    # 각 위치마다 확인
    for i in range(size):
        for j in range(size):
            ice_cnt = 0
            # 주변에 얼음있는지 살펴보기
            for d in range(4):
                nr = i + dr[d]
                nc = j + dc[d]
                if 0 <= nr < size and 0 <= nc <size:
                    if ice[nr][nc] > 0:
                        ice_cnt += 1
                        
            # 얼음이 있는데 주변에는 3 미만이라면 
            if ice_cnt < 3 and ice[i][j] != 0:
                melting_list.append((i, j))
    
    for i, j in melting_list:
        ice[i][j] = ice[i][j]-1
        
    return ice
                
def bfs(ice): # 가장 큰 얼음판 크기 확인
    visited = [[0 for _ in range(size)] for _ in range(size)]
    max_area = 0
    
    # 모든 칸에서 판 크기 확인
    for i in range(size):
        for j in range(size):
            area = 0 
            if visited[i][j] == 0 and ice[i][j] != 0: # 방문한 적 없고 얼음이 있는 칸
                queue = deque()
                queue.append((i,j))
                visited[i][j] = 1
                
                while queue:
                    i, j = queue.popleft()
                    area += 1
                    
                    for d in range(4):
                        ni = i + dr[d]
                        nj = j + dc[d]
                        # 판 안에 있고 방문한 적이 없고 얼음이 있다면
                        if 0<= ni < size and 0 <= nj < size and visited[ni][nj] == 0 and ice[ni][nj]:
                            visited[ni][nj] = 1
                            queue.append((ni, nj))
            
            max_area = max(max_area, area)
            
    return max_area 
                            

for L in L_list:
    ice = ice_rotate(ice, L) 
    ice = ice_melting(ice) 
    
max_area = bfs(ice)

print(sum([sum(i) for i in ice]))
print(max_area)

