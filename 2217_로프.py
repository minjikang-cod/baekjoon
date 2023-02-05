import sys
input = sys.stdin.readlines

ropes = []
weight = []
line = input()
N = int(line[0])
for i in line[1:]:
    ropes.append(int(i))

ropes.sort()
for r in range(len(ropes)):
    weight.append(ropes[r]*(N-r))
print(max(weight))