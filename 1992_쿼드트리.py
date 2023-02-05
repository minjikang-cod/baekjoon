import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
video = []
for _ in range(N):
    v = [int(x) for x in list(input().rstrip())]
    video.append(v)

def quadtree(n, vlist):
    s = 0
    for l in vlist:
        s += sum(l)
    
    if s == n**2:
        return '1'
    if s == 0:
        return '0'
    
    half = n//2
    temp = '('
    temp += quadtree(half,[l[:half] for l in vlist[:half]])
    temp += quadtree(half,[l[half:] for l in vlist[:half]])
    temp += quadtree(half,[l[:half] for l in vlist[half:]])
    temp += quadtree(half,[l[half:] for l in vlist[half:]])
    temp += ')'
    
    return temp

def quadtree2(n, row, col):
    s = 0
    for v in video[row:row+n]:
        s += sum(v[col:col+n])
    
    if s == n**2:
        return '1'
    if s == 0:
        return '0'
    
    half = n//2
    temp = '('
    temp += quadtree2(half,row, col)
    temp += quadtree2(half,row, col+half)
    temp += quadtree2(half,row+half, col)
    temp += quadtree2(half,row+half, col+half)
    temp += ')'
    
    return temp

#print(quadtree(N, video))
print(quadtree2(N, 0, 0))
