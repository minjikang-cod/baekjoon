import sys
input = sys.stdin.readlines

lines = input() 
N, B = map(int, lines[0].split())
mat = []
for l in lines[1:]:
    mat.append(list(map(int, l.split())))

def multiply(A, B):
    global N
    new = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                new[i][j] += A[i][k]*B[k][j]
            new[i][j] %= 1000
    return new

def divide(A, k):
    if k == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    if k == 2:
        return multiply(A, A)
    d = divide(A,k//2)
    if k%2:
        return multiply(multiply(d, d), A) 
    else:
        return multiply(d, d)
    
result = divide(mat, B)

for r in result:
    print(' '.join(map(str, r)))