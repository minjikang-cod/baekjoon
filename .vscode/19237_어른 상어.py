import sys
input = sys.stdin.readline 

N, M, k = map(int, input().split())
direction = {1:(-1,0), 2:(1,0), 3:(0,-1), 4:(0, 1)} # 상 하 좌 우 
board = [[0 for _ in range(N)] for _ in range(N)]
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]
shark = {}
for i in range(N):
    l = list(map(int, input().split()))
    for j in range(N):
        if l[j]:
            board[i][j] = l[j] # 보드에 추가
            shark[l[j]] = [i, j] # 상어 정보
            smell[i][j] = [l[j], k] # [상어번호, 냄새] 

#상어 방향
s_direction = list(map(int, input().split()))
for i in range(M):
    shark[i+1].append(s_direction[i])

# 상어 방향 우선순위 
sd_priority = {}
for i in range(M):
    sd = {}
    for j in range(4):
        sd[j+1] = list(map(int, input().split()))
    sd_priority[i+1] = sd

# 상어 이동
cnt = 0
while len(shark) > 1:
    cnt += 1
    if cnt > 1000: cnt = -1 ;break
    
    for i in range(1, M+1):
        if i in shark:
            x, y, d = shark[i][0], shark[i][1], shark[i][2]
            pr =sd_priority[i][d] # 상어 방향에서의 우선순위
            is_back = [] # 다시 돌아갈 곳의 정보
            for p in pr:
                dx, dy = direction[p]
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < N:
                    if smell[nx][ny] == [0,0]: # 아무 냄새가 없는 칸
                        shark[i] = [nx, ny, p] # 샤크 다음 위치 정보 저장
                        if board[nx][ny] == 0: # 혼자면
                            board[nx][ny] = i
                        elif board[nx][ny] > i: # 나보다 더 숫자가 큰 상어가 있었다면
                            del shark[board[nx][ny]]
                            board[nx][ny] = i
                        else:
                            del shark[i]
                        #board[nx][ny].append(i+1)
                        #board[x][y].pop(0) # 칸에 앞에 원래 저장되어있던 상어 치워
                        is_back = [] # 돌아갈 칸 따위 없어
                        break
                    
                    elif smell[nx][ny][0]==i and not is_back: # 내가 지나왔던 칸
                        is_back = [nx, ny, p]
                        continue
            
            if is_back: # 다시 돌아간다면
                nx, ny, p = is_back[0], is_back[1], is_back[2]
                shark[i] = [nx,ny,p]
                if board[nx][ny] == 0: # 혼자면
                    board[nx][ny] = i
                elif board[nx][ny] > i: # 나보다 더 숫자가 큰 상어가 있었다면
                    del shark[board[nx][ny]]
                    board[nx][ny] = i
                else:
                    del shark[i]
            
            board[x][y] = 0 # 원래 있던 자리의 상어 지우기

    for i in range(N):
        for j in range(N):
            # 냄새 하나씩 지우기
            if smell[i][j][1] > 1: # 냄새가 1 이상
                smell[i][j][1] -= 1
            elif smell[i][j][1] == 1: # 냄새 1
                smell[i][j] = [0, 0]
            
            # 새로운 상어판 업데이트 
            if board[i][j]:
                smell[i][j] = [board[i][j], k] # 새로운 냄새 풍기기

print(cnt)      
                
                
            
            
    
    