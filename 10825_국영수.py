import sys
input = sys.stdin.readlines

score = []
for i in input()[1:]:
    name, korean, english, math = i.split()
    score.append([name, korean, english, math])

score.sort(key = lambda x : (-1*int(x[1]),int(x[2]), -1*int(x[3]), x[0]))

for i in score:
    print(i[0])