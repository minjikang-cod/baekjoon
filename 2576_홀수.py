import sys

numbers = []

for i in range(7):
    new = int(sys.stdin.readline())
    if new % 2 == 1:
        numbers.append(new)
        
if len(numbers) == 0:
    print(-1)
else:
    print(sum(numbers))
    print(min(numbers))