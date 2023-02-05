from collections import defaultdict
import sys
input = sys.stdin.readline

num_card = defaultdict(int)
n = int(input())

for _ in range(n):
    num = int(input())
    num_card[num] += 1

num_card = sorted(num_card.items(), key = lambda x: (-x[1],x[0]))

print(num_card[0][0])