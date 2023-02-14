import sys
from collections import deque

N, M = map(int, input().split())
visited = [-1] * 101
ladder = {}
snake = {}
for _ in range(N):
    i, j = map(int, input().split())
    ladder[i] = j
for _ in range(M):
    i, j = map(int, input().split())
    snake[i] = j
    
queue = deque([1])
visited[1] = 0

while queue:
    now = queue.popleft()
    for d in range(1, 7):
        next = now + d
        if next <= 100 and visited[next] == -1: # 이동한 위치가 100이하이고 방문한 적 없으면
            # 사다리나 뱀에 있으면 위치 변경
            if next in ladder:
                next = ladder[next]
            if next in snake:
                next = snake[next]
            
            #이동했을 수 있으니 방문여부 한번 더 확인
            if visited[next] == -1:
                queue.append(next)
                visited[next] = visited[now] + 1

print(visited[100])
