import sys
input = sys.stdin.readline
MAX = 1000000007

n = int(input())
basic = [[0,1],[1,1]]

def multiply(A, B):
    #global N
    new = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                new[i][j] += A[i][k]*B[k][j]
            new[i][j] %= MAX
    return new

def divide(A, k):
    if k == 1:
        for i in range(2):
            for j in range(2):
                A[i][j] %= MAX
        return A
    if k == 2:
        return multiply(A, A)
    d = divide(A,k//2)
    if k%2:
        return multiply(multiply(d, d), A) 
    else:
        return multiply(d, d)

result = divide(basic, n)

print(result[1][0])