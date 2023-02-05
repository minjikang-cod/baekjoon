import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
answer = []

def find_sequence(before, count, arr = []):
    for i in range(before+1, N+1):
        temp = copy.deepcopy(arr)
        temp.append(i)
        
        if count == 1:
            answer.append(temp)
        else:
            find_sequence(i, count-1, temp)

find_sequence(0, M)
for a in answer:
    print(' '.join(map(str, a)))
    
# 그냥 itertools 조합(Combinations) 이용하면 돼
from itertools import combinations
arr = [i+1 for i in range(N)]
for a in combinations(arr, M):
    print(*a)