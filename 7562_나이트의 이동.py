from collections import deque
import sys
input = sys.stdin.readlines

lines = input()
i = 1
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for _ in range(int(lines[0])):
    I = int(lines[i])
    grid = [[-1 for _ in range(I)] for _ in range(I)]
    start = list(map(int, lines[i+1].split()))
    end = list(map(int, lines[i+2].split()))
    
    queue = deque()
    queue.append(start)
    grid[start[0]][start[1]] = 0
    
    while queue:
        x, y = queue.popleft()
        if x == end[0] and y == end[1]: 
            print(grid[end[0]][end[1]])
            break
        for j in range(8):
            xx = x + dx[j]
            yy = y + dy[j]
            if 0 <= xx < I and 0 <= yy < I and grid[xx][yy] == -1:
                queue.append((xx,yy))
                grid[xx][yy] = grid[x][y] + 1
    
    print(grid[end[0]][end[1]])
    i += 3