import sys
import copy
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
sequence = []
check = [0]*(N+1)
def find_sequence(arr, check, count):
    if count == M:
        temp = copy.deepcopy(arr)
        sequence.append(temp)
    else:
        for i in range(1, N+1):
            if check[i] == 0:
                check[i] = 1
                arr.append(i)
                find_sequence(arr, check, count+1)
                check[i] = 0
                arr.pop()

for a in permutations(map(str, range(1,N+1)),M):
    print(' '.join(a))

#find_sequence([], check, 0)
#for s in sequence:
#    print(" ".join(map(str, s)))