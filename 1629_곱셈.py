# 모듈로 연산

import sys 
input = sys.stdin.readline

A,B,C = map(int, input().split())

def mul(a,n):
    if n==1:
        return a%C
    else:
        k = mul(a,n//2)
        if n%2==0:
            return (k*k)%C
        else:
            return (k*k*a)%C
    
print(mul(A,B))