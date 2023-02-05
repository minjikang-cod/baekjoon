import sys
from itertools import product
#import copy
input = sys.stdin.readline

N, M = map(int, input().split())

for a in product(map(str,range(1,N+1)), repeat = M):
    print(' '.join(a))

# 시간 초과
#answer = []
#def find_sequence(count, arr = []):
#    for i in range(1, N+1):
#        temp = copy.deepcopy(arr)
#        temp.append(i)
#        
#        if count == 1:
#            answer.append(temp)
#        else:
#            find_sequence(count-1, temp)

#find_sequence(M)
#for a in answer:
#    print(*a)
