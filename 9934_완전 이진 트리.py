import sys
input = sys.stdin.readlines

lines = input()
tree = [[] for _ in range(int(lines[0]))]
inorder = list(map(int, lines[1].split()))

def tree_depth(start, end, i):
    if start > end:
        return 
    mid = (start+end)//2
    tree[i].append(inorder[mid])
    tree_depth(start, mid-1,i+1)
    tree_depth(mid+1, end,i+1)

tree_depth(0, len(inorder)-1,0)
for t in tree:
    print(' '.join(map(str, t)))