import sys

inp = sys.stdin.readline
n = int(inp())
grade = [1 for _ in range(n)]

weight = [0 for _ in range(n)]
height = [0 for _ in range(n)]

for i in range(n):
    weight[i], height[i] = map(int, inp().split())
    
for i in range(n):
    for j in range(n):
        if weight[i] < weight[j] and height[i] < height[j]:
            grade[i] = grade[i]+1

print(" ".join(list(map(str,grade))))
    