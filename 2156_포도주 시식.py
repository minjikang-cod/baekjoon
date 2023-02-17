import sys
input = sys.stdin.readline

lines = input()
N = int(lines[0])
grape = [0] + [int(lines[i]) for i in range(1, N+1)] + [0]
drink = [0]*(N+2)
# 포도주는 1개부터 올 수 있어!!! 2번째 원소를 입력받지 않아도 처리할 수 있도록 고려가 필요해 
drink[1], drink[2] = grape[1], grape[1]+grape[2]

for i in range(3,N+1):
    drink[i] =  max(drink[i-1], # 지금 안 마신다
                    drink[i-2]+grape[i], # 이전 안 마시고, 지금 마신다
                    drink[i-3]+grape[i-1]+grape[i]) # 이전, 지금 모두 마신다

print(drink[N])

'''

6 10 13 9 8 1
6 : 6
10 : 6+10
13 : 6+13/ 0+10+13
9 : 6+13+9/16+9
8 : 8+23 / 8+9+16 = 33
1 : 1+28 / 1+8+23

'''

'''

# n이 1부터인 경우를 생각해야해!!
n = int(input())
drink = [0]*100001
for i in range(1,n+1):
    drink[i] = int(input())
dp = [0]*100001
dp[1], dp[2] = drink[1], drink[1]+drink[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-1], # 지금 안 마신다
                drink[i]+dp[i-2], # 이전 안 마시고, 지금 마신다
                drink[i]+drink[i-1]+dp[i-3]) # 이전, 지금 모두 마신다
print(dp[n])

'''