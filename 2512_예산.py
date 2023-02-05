import sys
input = sys.stdin.readlines

lines = input()
N = int(lines[0])
budget_list = list(map(int, lines[1].split()))
M = int(lines[2])

start, end = 0, max(budget_list)

while start <= end:
    sum_budget = 0
    mid = (start+end)//2
    for b in budget_list:
        sum_budget += min(mid, b)
    if sum_budget == M:
        end = mid;break
    elif sum_budget > M: 
        end = mid-1
    else:
        start = mid+1

print(end)