from collections import deque
import sys
input = sys.stdin.readlines
    
lines = input()
num_node = int(lines[0].rstrip())
parents = [0]*(num_node+1)
parents[1] = 1 # 루트 노드 부모 미리 임의 지정
rel = {i:[] for i in range(1,num_node+1)}
queue = deque([1])

for l in lines[1:]:
    a, b = map(int, l.split())
    rel[a].append(b);   rel[b].append(a)

while queue:
    p = queue.popleft()
    for r in rel[p]:
        if not parents[r]:   # 부모 지정이 아직 안된 노드라면
            queue.append(r) # queue에 추가하고 부모 노드를 현재 노드로 지정
            parents[r]=p 

print('\n'.join(map(str, parents[2:])))