import sys
input = sys.stdin.readlines
sys.setrecursionlimit(10**6)

tree = []
for i in input():
    tree.append(int(i.rstrip()))

def postorder(start, end): # start, end index를 각각의 input으로 받아들임 
    if start > end:
        return
    
    current = tree[start] # 현재 기준 node
    
    if current > tree[end]: # 모두 현재 node보다 작으면 (맨 끝이 가장 큰 값을 가지는 node임)*****
        postorder(start+1, end)
        print(current)
        return 
    
    mid = end + 1 # 문제를 분할할 기준 중간 node
    for i in range(start+1, end+1):
        if current < tree[i]: # 현재 기준 node보다 큰 값이 나오면 그때부터는 다 큰 값
            mid = i 
            break
    # post order : 좌 - 우 - 부모
    postorder(start+1, mid-1) # 현재 기준 좌측
    postorder(mid,end) # 현재 기준 우측
    print(current) # 현재 노드 출력
    
postorder(0,len(tree)-1)
