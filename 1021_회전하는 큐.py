from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cycle = deque([i+1 for i in range(N)])
num_list = list(map(int, input().split()))
total_count = 0

for num in num_list:
    if cycle[0]==num:
        cycle.popleft()
    else:
        left = cycle.index(num)
        right = len(cycle) - cycle.index(num)
        if left > right:
            cycle.rotate(right)
            total_count += right
        else:
            cycle.rotate(-left)
            total_count += left
        cycle.popleft()
            
print(total_count)