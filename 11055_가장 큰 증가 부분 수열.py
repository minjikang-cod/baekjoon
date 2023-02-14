import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
dp = list(num_list)

for i in range(1,N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            temp = dp[j]+num_list[i]
            if temp > dp[i]: dp[i] = temp

print(max(dp))