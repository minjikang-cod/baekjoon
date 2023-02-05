import sys
input = sys.stdin.readlines
sys.setrecursionlimit(100000000)
    
lines = input()
num_node = int(lines[0].rstrip())
parents = [0]*(num_node+1)
rel = {i:[] for i in range(1,num_node+1)}

for l in lines[1:]:
    a, b = map(int, l.split())
    rel[a].append(b);   rel[b].append(a)

def find_parents(p):
    for r in rel[p]:
        if r != 1 and not parents[r]: 
            parents[r] = p
            find_parents(r)
    return

find_parents(1)

for i in range(2,len(parents)):
    print(parents[i])
