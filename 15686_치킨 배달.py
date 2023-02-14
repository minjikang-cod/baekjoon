import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
chicken = []
house = []
select = []
for i in range(N): # 치킨, 집 정보 저장
    s = list(map(int, input().split()))
    for j in range(N):
        if s[j] == 1:
            house.append([i, j])
        elif s[j] == 2:
            chicken.append([i,j])
result = 10e9

def choose_chicken(select, idx, cnt):
    global result
    if cnt == M: # 치킨집을 M개 골랐을 때
        dist = cal_dist(select,house) # 치킨 거리 측정
        result = dist if result > dist else result # 최솟값 업데이트
        return

    for i in range(idx, len(chicken)):
        select.append(chicken[i])
        choose_chicken(select, i+1, cnt+1)
        select.pop()
        

def cal_dist(chicken, house):
    dists = []
    for h in house:
        min_dist = 10e9
        for c in chicken: # 모든 치킨집에서의 거리 중 가장 짧은 거리를 가지는 치킨집 선택
            dist = abs(h[0]-c[0]) + abs(h[1]-c[1])
            min_dist = dist if dist < min_dist else min_dist
        dists.append(min_dist)
    
    return sum(dists)

choose_chicken(select, 0, 0)
print(result)
