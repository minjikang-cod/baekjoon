import sys
from heapq import heappush, heappop
input = sys.stdin.readlines

lines = input()
N = int(lines[0]); M = int(lines[1])
# 버스정보 저장(도착지와 버스 비용)
bus_list = [[]for _ in range(N+1)]
for l in lines[2:2+M]:
    a,b,w = map(int,l.split())
    bus_list[a].append([b, w])

start, end = map(int, lines[-1].split())
hq = []
heappush(hq, (0, start))
total_cost = [10**8]*(N+1)
total_cost[start] = 0

while hq:
    cost, city = heappop(hq)
    # 이미 최소비용이 나왔다면 pass
    if total_cost[city] < cost:
        continue
    for bus in bus_list[city]:
        # 출발지까지의 cost + 이동비용
        ncost = total_cost[city] + bus[1]
        # 더 적은 비용이 발생한다면 갱신하면서 힙큐에 집어넣기
        if ncost < total_cost[bus[0]]:
            total_cost[bus[0]] = ncost
            heappush(hq, (ncost,bus[0]))
        
print(total_cost[end])