import sys
input = sys.stdin.readlines
from heapq import heappop, heappush

line = input()
N = int(line[0])
time = []
queue = []

for l in line[1:]:
    start, end = map(int, l.split())
    time.append([start,end])
time.sort(key=lambda x : x[0])

heappush(queue, time[0][1])
for i in range(1, N):
    if time[i][0]  >= queue[0]:
        heappop(queue)
    heappush(queue, time[i][1])

print(len(queue))
