import sys
input = sys.stdin.readline

def make_matrix():
    matrix = []
    m, n = map(int, input().split())
    for _ in range(m):
        matrix.append(list(map(int, input().split())))

    return m, n, matrix 

A_m, A_n, A = make_matrix() 
B_m, B_n, B = make_matrix() 

result = [[0 for _ in range(B_n)] for _ in range(A_m)]

for i in range(A_m):
    for j in range(B_n):
        for k in range(A_n):
            result[i][j] += A[i][k]*B[k][j]

for r in result:
    print(' '.join(map(str, r)))