from heapq import heappush, heappop
import sys
input = sys.stdin.readlines 

heap=[]
for i in input()[1:]:
    num = int(i)
    if num != 0:
        heappush(heap,(abs(num),num))
    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)