import sys
input = sys.stdin.readline

N = int(input())
num = [0]*2000001

for _ in range(N):
    num[int(input())+1000000] = 1

print('\n'.join([str(i-1000000) for i in range(2000001) if num[i]]))
    
