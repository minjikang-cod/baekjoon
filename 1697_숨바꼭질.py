import sys
input = sys.stdin.readline
from collections import deque

subin, sister = map(int, input().split())
MAX = 100000
days = [0] * (MAX+1)
queue = deque()

def find_sister(x, goal): #현재 위치와 목표
    queue.append(x)
    days[x] = 1
    present = -1
    while queue:
        present = queue.popleft()
        if present == goal: break
        for next in (present-1, present+1, 2*present): 
            if 0<=next<=MAX and days[next] == 0:
                queue.append(next); days[next] = days[present]+1
                    
find_sister(subin, sister)
print(days[sister]-1)
