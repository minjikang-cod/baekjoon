import sys
input = sys.stdin.readlines
limit_number = 10**6
sys.setrecursionlimit(limit_number)

lines = input()
N, M, R = map(int, lines[0].split())
edge = {i:[] for i in range(1,N+1)}
visit = [0] * (N+1)
path = []

for l in lines[1:]:
    p1, p2 = map(int, l.split())
    edge[p1].append(p2)
    edge[p2].append(p1) 
    
for key, value in edge.items():
    edge[key] = sorted(value)

def dfs(start):
    visit[start] = 1
    path.append(start)
    
    for e in edge[start]:
        if visit[e]==0: 
            dfs(e)
        
dfs(R)

print(path)
result = []
for idx, node in enumerate(path):
    result
