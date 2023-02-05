import sys
input = sys.stdin.readlines

lines = input()
N, M = map(int, lines[0].split())
tree = list(map(int, lines[1].split()))

start, end = 1, max(tree)

while start <= end:
    mid = (start+end)//2
    
    sum_tree = 0
    for t in tree:
        sum_tree += max(0, t-mid)
    
    if sum_tree >= M: start = mid+1
    else: end = mid-1

print(end)