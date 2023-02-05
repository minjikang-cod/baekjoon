import sys

inp = sys.stdin.readline
series = int(inp())

count = 0
number = 666

while count < series:
    if "666" in str(number):
        count += 1
    number += 1

print(number-1)


