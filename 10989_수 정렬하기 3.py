import sys

n = int(sys.stdin.readline())
number = {}

for i in range(n):
    new = int(sys.stdin.readline())
    if new in number:
        number[new] += 1
    else:
        number[new] = 1
    
for key in sorted(number.keys()):
    for _ in range(number[key]):
        print(key)