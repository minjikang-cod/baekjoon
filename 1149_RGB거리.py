import sys
input = sys.stdin.readlines

cost = []
for i in input()[1:]:
    cost.append(list(map(int, i.split()))) 

for i in range(1, len(cost)):
    # 0 : red / 1 : green / 2 : blue
    cost[i][0] = cost[i][0] + min(cost[i-1][1], cost[i-1][2])
    cost[i][1] = cost[i][1] + min(cost[i-1][0], cost[i-1][2])
    cost[i][2] = cost[i][2] + min(cost[i-1][0], cost[i-1][1])
    
print(min(cost[-1])) 