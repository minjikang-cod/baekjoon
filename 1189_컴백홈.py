import sys
input = sys.stdin.readline

R,C,K = map(int, input().split())
map = [input().rstrip() for _ in range(R)]

visited = [[0 for _ in range(C)] for _ in range(R)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = 0

def gohome(x, y, cnt):
    global answer, visited
    if x == 0 and y == C-1: # 집에 도착
        if cnt == K: # K번 걸려 집 갔을때만 더하기
            answer += 1
        return 
    if cnt > K: # 더 오래 걸릴 것 같으면 그냥 끝내
        return 
        
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i] 
        if 0<=nx<R and 0<=ny<C and map[nx][ny] != 'T' and visited[nx][ny]==0:
            visited[nx][ny] = 1
            gohome(nx, ny, cnt+1)
            visited[nx][ny] = 0 

visited[R-1][0] = 1
gohome(R-1, 0, 1)
print(answer)