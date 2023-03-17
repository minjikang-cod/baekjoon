import sys 
input = sys.stdin.readlines

l = input() 
N = int(l[0])
words = sorted([w.rstrip() for w in l[1:]], key = lambda x : len(x))

prefix = 0
for i in range(N):
    for j in range(i+1,N): # 현재 길이 기준 나보다 긴 단어들에 대해
        if words[i] == words[j][:len(words[i])]: # 긴 단어의 앞이 짧은 단어랑 같다면
            prefix += 1
            break 

print(N-prefix)