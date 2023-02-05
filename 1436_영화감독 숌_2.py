import sys

inp = sys.stdin.readline
series = int(inp())

count = 0

box = [0,0,0]

while True:
    case = len(box)-3
    if case == 0:
        count += 1
    else:
        for i in range(len(box)-2):
            box[i:i+3]=6
            #box[]    