import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
paper = []
for _ in range(N):
    p = list(map(int, input().rstrip().split()))
    paper.append(p)

def divide_paper(n,row, col):
    global cnt
    first = paper[row][col]
    # 원소가 1개면
    if n == 1:
        cnt[first] += 1
        return 
    # 영역 내에 다른 수가 존재하는지 확인
    for i in range(row, row+n):
        for j in range(col, col+n):
            if paper[i][j] != first:
                tri = n//3 
                for i in range(3):
                    for j in range(3):
                        divide_paper(tri, row+i*tri, col+j*tri)
                return
    # 없으면 하나의 종이로 판단
    cnt[first] += 1

cnt = [0]*3
divide_paper(N, 0, 0)

for num in range(-1,2):
    print(cnt[num])