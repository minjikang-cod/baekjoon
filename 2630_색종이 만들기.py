import sys
input = sys.stdin.readlines

lines = input()
N = int(lines[0])

paper = []

for l in lines[1:]:
    paper.append(list(map(int, l.split())))

def blue_white(n, paper):
    if n==1: # 한칸이면 그 칸의 색깔 따라 return
        if paper[0][0]==1: return 1, 0
        else: return 0, 1
    
    temp_sum = 0
    for i in range(n):
        temp_sum += sum(paper[i])
    
    if temp_sum == n**2: # 모두 파랑색이면
        return 1, 0
    elif temp_sum == 0: # 모두 흰색이면
        return 0, 1
    else:
        # 가로세로 2등분하여 구한 후 총합
        b1, w1 = blue_white(n//2, [p[:n//2] for p in paper[:n//2]])
        b2, w2 = blue_white(n//2, [p[n//2:] for p in paper[:n//2]])
        b3, w3 = blue_white(n//2, [p[:n//2] for p in paper[n//2:]])
        b4, w4 = blue_white(n//2, [p[n//2:] for p in paper[n//2:]])
        
        return b1+b2+b3+b4, w1+w2+w3+w4

bb, ww = blue_white(N, paper)
print(ww)
print(bb)