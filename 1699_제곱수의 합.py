import sys 
input = sys.stdin.readline

N = int(input())
dp = [i for i in range(N+1)] # 초기화 : 1만으로 구성하기(가장 많은 경우의 수를 표현할 수 있음)
for i in range(1, N+1):
    for j in range(1, i):
        if j**2 > i: break # 제곱수가 i보다 크면 나가기
        if dp[i] > dp[i-j**2] + 1: # 제곱수만큼 작은 수에 대한 dp 값에서 +1
            dp[i] = dp[i-j**2] + 1 # min 연산 대신 비교연산

print(dp[N])