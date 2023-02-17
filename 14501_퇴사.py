import sys 
input = sys.stdin.readline 

N = int(input())
consult = [list(map(int, input().split())) for _ in range(N)] # [time, money] 정보 저장
profit = [0]*21

for i in range(N):
    time, money = consult[i][0], consult[i][1]
    profit[i+time] = max(profit[i+time], max(profit[:i+1])+money)
    
print(max(profit[:N+1]))







'''
1   2   3   4   5   6   7   8   9   10  11
                    50  60      80       90
            


'''