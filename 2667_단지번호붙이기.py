import sys
from collections import deque
input = sys.stdin.readlines

line = input()
N = int(line[0].strip())
map = []
for line in line[1:N+1]:
    m = list(line.strip())
    map.append([int(i) for i in m])
num_house = []
queue = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    for j in range(N):
        if map[i][j]==1:
            queue.append((i,j))
            map[i][j]=0
            count = 1
            while queue:
                px, py = queue.popleft()
                for d in range(4):
                    xx = px + dx[d]
                    yy = py + dy[d]
                    if 0<=xx<N and 0<=yy<N and map[xx][yy]:
                        queue.append((xx,yy))
                        map[xx][yy]=0
                        count += 1
            num_house.append(count)

print(len(num_house))
for k in sorted(num_house):
    print(k)