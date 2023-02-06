import sys
input = sys.stdin.readlines

lines = input() 
N = int(lines[0])
ground = []
for l in lines[1:]: # 초기 설정 저장
    ground.append(list(map(int, l.split())))

x, y = N//2, N//2 # 시작 지점
move = 1 # 이동해야 하는 칸 수
dx = [0,1,0,-1] # 이동하는 방향 순서
dy = [-1,0,1,0]
out = 0 # 밖으로 나가는 양

def sand_movement(sx, sy, lx, ly):
    sa = [0.01, 0.01, 0.07, 0.07, 0.02, 0.02, 0.1, 0.1, 0.05] # 날라가는 비율
    temp = 0 # 비율 칸으로 날라가는 모래의 양 중간 저장 
    o = 0
    
    for xx, yy, aa in zip(sx, sy, sa):
        amount = int(ground[nx][ny]*aa)
        if 0 <= xx < N and 0 <= yy < N: # 격자 안이라면
            ground[xx][yy] = ground[xx][yy] + amount
        else: # 격자 밖이라면
            o += amount
        temp += amount
    if 0 <= lx < N and 0 <= ly < N: # 격자 안이라면
        ground[lx][ly] = ground[lx][ly] + (ground[nx][ny]-temp) # 마지막 알파 채우기 
    else: # 격자 밖이라면
            o += ground[nx][ny]-temp
    ground[nx][ny]=0 # 토네이도 맞은 땅 모래 다 없애기 
    
    return o


while move < N:
    for i in range(4):
        for m in range(move):
            nx, ny = x + dx[i], y + dy[i] # 다음 이동할 위치
            if ground[nx][ny] != 0: # 모래가 있다면
                # 모래를 날려보자
                if dx[i] != 0: # 세로로 이동할 경우
                    sx = [x, x, nx, nx, nx, nx, nx+dx[i], nx+dx[i], nx+2*dx[i]]
                    sy = [y+1, y-1, y+1, y-1, y+2, y-2, y+1, y-1, y]
                    lx, ly = nx+dx[i], y
                else: # 가로로 이동할 경우
                    sx = [x+1, x-1, x+1, x-1, x+2, x-2, x+1, x-1, x]
                    sy = [y, y, ny, ny, ny, ny, ny+dy[i], ny+dy[i], ny+2*dy[i]]
                    lx, ly = x, ny+dy[i]
                
                out = out + sand_movement(sx, sy, lx, ly)
            x, y = nx, ny
            #print(nx, ny)
        
        if i%2 != 0: # 두번씩 이동하고 이동량 늘리기
            move += 1

for m in range(N):
    if ground[nx][ny] != 0: # 모래가 있다면
        # 모래를 날려보자 - 마지막 가로 이동
        sx = [x+1, x-1, x+1, x-1, x+2, x-2, x+1, x-1, x]
        sy = [y, y, ny, ny, ny, ny, ny+dy[0], ny+dy[0], ny+2*dy[0]]
        lx, ly = x, ny+dy[0]
        out = out + sand_movement(sx, sy, lx, ly)
    nx = x + dx[0]
    ny = y + dy[0]
    x, y = nx, ny

print(out)
