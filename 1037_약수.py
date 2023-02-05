import sys
input = sys.stdin.readline

num_divisor = int(input())

real_divisor = list(map(int, input().split()))
number = min(real_divisor) * max(real_divisor)

print(number)