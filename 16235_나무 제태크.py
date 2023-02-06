import sys
input = sys.stdin.readline 

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
N, M, K = map(int, input().split())
A = [] # 매번 들어가는 양분
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)
ground = [[5 for _ in range(N)] for _ in range(N)] # 땅
tree = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    _x, _y, _age = map(int, input().split())
    tree[_x-1][_y-1].append(_age)

for _ in range(K): # K년 동안
    # 봄 여름
    for i in range(N):
        for j in range(N):
            if tree[i][j]: # tree가 있으면
                tree[i][j].sort() 
                next_tree = [] # 다음 해에도 갈 나무
                dead = 0 # 죽어서 양분으로 갈 나무의 나이
                for t in tree[i][j]:
                    if t <= ground[i][j]: # 현재 양분보다 작으면
                        next_tree.append(t+1)
                        ground[i][j] = ground[i][j]-t
                    else: # 양분이 부족하면
                        dead += t//2
                ground[i][j] += dead # 죽은 나무가 여름에 양분으로 추가
                tree[i][j] = next_tree
                
    # 가을
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                for t in tree[i][j]:
                    if t%5 == 0: # 나무 나이가 5의 배수이면
                        for d in range(8):
                            ni = i + dx[d]
                            nj = j + dy[d]
                            if 0 <= ni < N and 0 <= nj < N:
                                tree[ni][nj].append(1)
                            
    # 겨울
    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j] 
            
cnt = 0 
for i in range(N):
    for j in range(N):
        cnt += len(tree[i][j])
                
print(cnt)