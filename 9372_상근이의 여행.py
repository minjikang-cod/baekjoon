import sys
input = sys.stdin.readlines

sentences = input()
i=1
for _ in range(int(sentences[0].rstrip())):
    N, M = map(int,sentences[i].split()) 
    print(N-1)
    i += M+1
