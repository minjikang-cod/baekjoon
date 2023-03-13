import sys
input = sys.stdin.readline
MAX = 1000000000
N = int(input())

step = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def find_stepnumber(N):
    if N == 1:
        return sum(step[0])
    
    for i in range(1,N):
        temp = []
        for j in range(10):
            before = step[i-1][j-1] if j>0 else 0
            after = step[i-1][j+1] if j<9 else 0
            temp.append((before%MAX+after%MAX)%MAX)
        step.append(temp)
    
    return sum(step[N-1])%MAX

print(find_stepnumber(N))



'''
1 2 3 4 5 6 7 8 9
10,12   21,23    32,34   ...   87,89   98
101,121,123   210,212,232,234   321,323,343,345 ...  989,987

'''