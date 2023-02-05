import sys
from collections import deque
input = sys.stdin.readline

x, y = map(int, input().split())
map = []
queue = deque()
visited = [[0 for _ in range(y)] for _ in range(x)]
queue.append((0,0))
visited[0][0] = 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(x):
    line = list(input().strip())
    map.append([int(k) for k in line])

while queue:
    px, py = queue.popleft()
    count = visited[px][py] + 1
    
    for k in range(4):
        xx = px + dx[k]
        yy = py + dy[k]
        if 0 <= xx < x and 0 <= yy < y and map[xx][yy]:
            queue.append((xx,yy)); visited[xx][yy]=count; map[xx][yy] = 0
    
print(visited[x-1][y-1])
