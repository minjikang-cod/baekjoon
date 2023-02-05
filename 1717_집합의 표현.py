import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n+1)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def merge(a, b):
    a, b = find(a), find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
    
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        merge(b, c)
    else:
        if find(b) == find(c):
            print('YES')
        else:
            print('NO')