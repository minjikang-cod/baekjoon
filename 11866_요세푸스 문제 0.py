import sys

N, K = map(int, sys.stdin.readline().split())
result = []
nums = [i for i in range(1, N+1)]

idx = 0
while N > 0:
    idx = (idx+K-1) % N
    result.append(str(nums.pop(idx)))
    N -= 1
    
print('<' + ', '.join(result) + '>')