import sys
input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip() 
w, h = len(word1), len(word2)
lis = [[0 for _ in range(h+1)] for _ in range(w+1)]

for i in range(1, w+1):
    for j in range(1, h+1):
        # 같은 단어가 나오면
        if word1[i-1]==word2[j-1]:
            lis[i][j] = lis[i-1][j-1] + 1
        # 다른 단어일 때 
        else:
            lis[i][j] = max(lis[i-1][j], lis[i][j-1])
            
print(lis[-1][-1])