import sys 
input = sys.stdin.readline 

N = int(input())
dp = [0, 1, 1]

if N > 2:
    for i in range(3, N+1):
        dp.append(dp[-1]+dp[-2])

print(dp[N])
########################################
dp_zero = [0, 0, 1] # 0으로 끝나는 수 
dp_one = [0, 1, 0] # 1로 끝나는 수

if N > 2:
    for i in range(3, N+1):
        dp_one.append(dp_zero[i-1])
        dp_zero.append(dp_zero[i-1]+dp_one[i-1])

print(dp_zero[N]+dp_one[N])

'''
1

10

101
100

1010
1000
1001

10100
10000
10010
10101
10001

'''