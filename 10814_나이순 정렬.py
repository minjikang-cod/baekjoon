import sys
input = sys.stdin.readlines

information = []
for i in input()[1:]:
    age, name = i.split()
    information.append([age,name])

information.sort(key = lambda x : int(x[0]))

for i in information:
    print(' '.join(i))