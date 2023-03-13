import sys
from itertools import combinations
import re
input = sys.stdin.readline

N, K = map(int, input().split())
answer = 0

if K < 5:  # a, n, t, i, c
    print(0)
    
elif K >26:  # 알파벳 개수 26
    print(N)
    
else:
    K -= 5
    words = [0] * N 
    for i in range(N):
        temp = set(re.sub(r'[acint]','',input().rstrip()))
        for t in temp:
            words[i] |= (1 << (ord(t)-ord('a'))) # 알파벳 하나씩 비트마스킹
    
    candidate = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']
    # 조합 만들기
    for c in list(combinations(candidate, K)):
        each = 0
        cnt = 0
        # 조합 비트마스킹 만들기
        for i in c:
            each |= (1 << (ord(i)-ord('a')))
        
        # 단어와 조합의 비교
        for j in words:
            if each & j == j:
                cnt += 1
        
        # 최댓값 갱신
        if answer < cnt:
            answer = cnt
    
    print(answer)