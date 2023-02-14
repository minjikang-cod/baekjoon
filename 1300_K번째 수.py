import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

start, end = 1, N*N

while(start <= end):
    mid = (start+end)//2 # 중간값 설정
    
    cnt = 0
    for i in range(1, N+1):
        # i*j=임의의 값 이므로 각 행에서 행*열 곱한 값이 mid보다 작은 열의 개수를 더해준다. 
        cnt += min(mid//i, N)
        if cnt >= k:
            break
        
    if cnt >= k: # 더 많은 수가 존재하면 기준 수 줄이기
        end = mid - 1
    else: # 더 적은 숫자가 존재하면 기준 수 늘리기
        start = mid + 1

print(start)
