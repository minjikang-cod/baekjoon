import sys
input = sys.stdin.readlines

lines = input()
N = int(lines[0])
stairs = [0]*301
step = [0]*301

for i in range(1, N+1):
    stairs[i] = int(lines[i].rstrip())
    
step[1] = stairs[1] # 1번째 계단
step[2] = max(stairs[1]+stairs[2], stairs[2]) # 2번째 계단
step[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3]) # 3번째 계단

for i in range(4, N+1):
    # i-2번째 계단까지의 최대값 + 현재 계단의 가중치 (i-2번째 계단을 밟았다면 그 전은 신경 쓸 필요 없다)
    # i-3번째 계단까지의 최대값 + i-1번째 계단 가중치 + 현재 계단의 가중치 (i-1번째 게단을 밟았다면 i-2번째 계단은 밟으면 안된다)
    step[i] = max(step[i-2]+stairs[i], step[i-3]+stairs[i-1]+stairs[i])
    
print(step[N])