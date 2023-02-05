import sys
input = sys.stdin.readlines

tri = []
for i in input()[1:]:
    tri.append(list(map(int, i.split())))
    
for i in range(1, len(tri)): # 점수 업데이트
    for j in range(i+1):
        if j == 0: # 맨 왼쪽
            tri[i][j] = tri[i-1][j] + tri[i][j]
        elif j == i: # 맨 오른쪽
            tri[i][j] = tri[i-1][j-1] + tri[i][j]
        else: # 나머지
            tri[i][j] = max(tri[i-1][j-1],tri[i-1][j]) + tri[i][j]

print(max(tri[-1]))