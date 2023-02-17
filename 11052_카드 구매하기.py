import sys 
input = sys.stdin.readline 

N = int(input())
cost = [0]+list(map(int, input().split()))

for i in range(2, N+1):
    for j in range(i//2+1): # 숫자 기준 절반까지만 따져봐도 돼
        cost[i] = max(cost[i], cost[i-j]+cost[j])

print(cost[-1])
        

'''
1    2      3           4 
3
    5/3*2
          15/6+3/3*3  
                    16/15+3/6*2
                    
    2+0, 1+1
            3+0,2+1
                    4+0,3+1,2+2
                                5+0, 4+1, 3+2
                                            6,5,4,3
                                                        7,6,5,4
'''