import sys
input = sys.stdin.readlines

line = input()
A = list(map(int,line[1].strip().split()))
B = list(map(int,line[2].strip().split()))
sum = 0

A.sort()
B.sort(reverse=True)

for i in range(len(A)):
    sum += A[i]*B[i]
    
print(sum)