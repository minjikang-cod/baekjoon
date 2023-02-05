import sys
import math
input = sys.stdin.readline

space = int(input())
#viewer = space
candidates = list(map(int, input().split()))
first, second = map(int, input().split())

candidates = list(map(lambda x : math.ceil(max(0,x-first)/second), candidates))

#for i in range(space):
#    viewer += math.ceil(max(0,candidates[i]-first)/second)
viewer = space + sum(candidates)  

print(viewer)