# 인오더 : 좌 - 루 - 우
# 포스트오더 : 좌 - 우 - 루
# 프리오더 : 루 - 좌 - 우


# 1. 루트를 찾는다.(포스트오더의 맨 마지막)
# 2. 인오더에서 루트 기준 왼쪽이 트리 왼쪽에 있는 아이들, 루트 기준 오른쪽이 트리 오른쪽에 있는 아이들
# 3. 2번에서 개수를 세면 포스트오더에서 왼쪽에 있는 아이들, 오른쪽에 있는 아이들 나눌 수 있음

import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline 
        
def to_preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return 
    
    root = postorder[post_end] # 루트 노드는 포스트오더의 맨 마지막
    in_root = pos[root] # root 찾을 때 마다 시간 오래 걸리니까 위치 미리 저장해놓자 
    lefts = in_root-in_start
    
    print(root, end = ' ') # 1. 루트 출력
    to_preorder(in_start, in_root-1, post_start, post_start+lefts-1) # 2. 좌측
    to_preorder(in_root+1, in_end, post_start+lefts, post_end-1) # 3. 우측


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
pos = [0]*(n+1)
for i in range(n):
    pos[inorder[i]] = i

to_preorder(0, n-1, 0, n-1)