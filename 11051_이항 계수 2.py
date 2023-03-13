import sys
input = sys.stdin.readline

N, K = map(int, input().split())
K = min(K, N-K)
coef = [1, N]

if K >= 2:
    for i in range(2, K+1):
        coef.append(coef[-1]*(N-i+1)//i)

print(coef[K]%10007)