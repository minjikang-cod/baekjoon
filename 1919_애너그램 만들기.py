import sys
input = sys.stdin.readline

a = list(input())[:-1]
b = list(input())[:-1]
common = []

for i in a:
    if i in b:
        b.remove(i)
        common.append(i)

print(len(a)+len(b)-len(common))