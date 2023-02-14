import sys 
input = sys.stdin.readlines 

def dfs (sx, sy, go, amount):
    if go == 4: # 블럭 4개 모두 사용했으면
        tsum.add(amount)
        return
    for i in range(4):
        # 다음 방문할 좌표
        nx = sx + dx[i]
        ny = sy + dy[i]
        
        # 종이 위에 있고 방문한 적 없으면
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] ==0:
            visited[nx][ny] = 1
            dfs(nx, ny, go+1, amount+paper[nx][ny])
            visited[nx][ny] = 0

def another_shape(sx, sy): # ㅜ 모양 처리하기
    # ㅜ
    if 0<= sx < N-1 and 0 <= sy < M-2:
        tsum.add(paper[sx][sy] + paper[sx][sy+1] + paper[sx][sy+2] + paper[sx+1][sy+1])
    # ㅏ
    if 0<= sx < N-2 and 0 <= sy < M-1:
        tsum.add(paper[sx][sy] + paper[sx+1][sy] + paper[sx+2][sy] + paper[sx+1][sy+1])
    # ㅗ
    if 1<= sx < N and 0 <= sy < M-2:
        tsum.add(paper[sx][sy] + paper[sx][sy+1] + paper[sx][sy+2] + paper[sx-1][sy+1])
    # ㅓ
    if 0<= sx < N-2 and 1 <= sy < M:
        tsum.add(paper[sx][sy] + paper[sx+1][sy] + paper[sx+2][sy] + paper[sx+1][sy-1])

lines = input() 
N, M = map(int, lines[0].split())
paper = []
for l in lines[1:]:
    paper.append(list(map(int, l.split())))
visited = [[0 for _ in range(M)] for _ in range(N)] # 방문했는지 확인
tsum = set() # 합 저장
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0] # x, y 이동 방향

for i in range(N):
    for j in range(M): # 모든 칸 방문
        visited[i][j] = 1
        dfs(i, j, 1, paper[i][j])
        visited[i][j] = 0
        another_shape(i,j)
        
        
print(max(tsum))


