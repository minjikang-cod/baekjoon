import heapq
import sys
input = sys.stdin.readline

N = int(input())
gift = []

for _ in range(N):
  nums = list(map(int, input().split()))
  if nums[0] == 0:
    if len(gift) == 0:
      print(-1)
    else:
      print(heapq.heappop(gift)[1])
  else:
    for num in nums[1:]:
      heapq.heappush(gift,(-num,num))