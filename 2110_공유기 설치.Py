import sys
input = sys.stdin.readline

N, C = map(int, input().split())

apart = []
for _ in range(N):
    apart.append(int(input()))
apart.sort() # 아파트 작은 값부터 정렬

# 공유기 사이의 적정 거리를 이분탐색으로 찾을 예정
# 공유기 개수에 따라서 설치할 수 있는 적정 최대 거리를 end로 잡음
start, end = 1, 1 + (apart[-1]-apart[0])//(C-1)

result = 0

while start<=end:
    mid = (start+end)//2
    cnt = 1
    loc = apart[0] # 마지막으로 설치된 공유기 위치 
    
    for i in range(1, N):
        if apart[i]- loc >= mid: # 차이가 더 크거나 같으면 설치하고 공유기 위치 업데이트
            cnt += 1
            loc = apart[i]
            
    if cnt >= C: # 조건 이상의 공유기를 설치했다면(기준 거리 늘리기)
        start = mid + 1
        result = mid
    else: # C보다 작다면(기준 거리 줄이기)
        end = mid - 1
        
print(result)
            