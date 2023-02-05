from collections import deque, defaultdict
import sys

input = sys.stdin.readlines
inp = input()

check = [-1]*(int(inp[0])+1)
start, end = map(int,inp[1].split())
relation = defaultdict(list)
queue = deque()

for i in inp[3:]:
    a, b = map(int, i.split())
    relation[a].append(b)
    relation[b].append(a)

queue.append(start)
check[start] += 1

while queue:
    first = queue.popleft()
    if first == end:
        break
    for r in relation[first]:
        if check[r] == -1:
            queue.append(r)
            check[r] = check[first] + 1

print(check[end])