import sys
input = sys.stdin.readlines

lines = input()
N, S = map(int, lines[0].split())
num_list = list(map(int, lines[1].split()))

start, end = 0, 0

partial_sum = num_list[0]
min_length = N+1

while start < N and end < N:
    if partial_sum >= S:
        min_length = min(min_length, end-start+1)
        partial_sum -= num_list[start]
        start += 1
    else:
        end += 1
        if end == N:
            break
        partial_sum += num_list[end]

print(0) if min_length == N+1 else print(min_length)