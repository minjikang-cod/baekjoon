from heapq import heappush, heappop
import sys
input = sys.stdin.readlines

heap = []
for l in input()[1:]:
    num = int(l)
    if num != 0:
        heappush(heap,num)
    else:
        if heap:
            print(heappop(heap))
        else:
            print(0)