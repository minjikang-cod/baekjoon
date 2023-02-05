import sys
input = sys.stdin.readlines

session = []
for r in input()[1:]:
    s, e = map(int, r.split())
    session.append([s, e])
session.sort(key = lambda x : (x[1], x[0]))

now_end = session[0][1]
count = 1
for i in range(1,len(session)):
    if session[i][0] >= now_end:
        count += 1
        now_end = session[i][1]

print(count)
