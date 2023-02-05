import sys

n = int(sys.stdin.readline())
number = [0]*10001

for i in range(n):
    new = int(sys.stdin.readline())
    number[new] += 1
    
for i in range(len(number)):
    for _ in range(number[i]):
        print(i)