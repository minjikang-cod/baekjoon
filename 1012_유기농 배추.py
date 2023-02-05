import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(int(input())):
    queue = deque()
    M, N, K = map(int, input().split())
    cabbage = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        cabbage[x][y] = 1

    count = 0
    for i in range(M):
        for j in range(N):
            if cabbage[i][j]==1:
                cabbage[i][j] = 0 # 방문했으니까 0 처리
                queue.append((i,j))
                count += 1
                while queue:
                    ii, jj = queue.popleft()
                    for k in range(4):
                        di = ii + dx[k]
                        dj = jj + dy[k]
                        if 0 <= di < M and 0 <= dj < N and cabbage[di][dj]==1:
                            cabbage[di][dj] = 0 # 주변도 0처리
                            queue.append((di, dj))
    print(count)
