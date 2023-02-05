import sys
from itertools import permutations, combinations
input = sys.stdin.readlines

lines = input()
N = int(lines[0])
stats = []
for l in lines[1:]:
    stats.append(list(map(int, l.split())))

differ = 100

def cal_combi(idx, start = []):
    global differ
    if idx == N//2:
        link = list(set(range(N))-set(start))
        s_sum, l_sum = 0, 0
        for i in range(N//2-1):
            for j in range(i+1, N//2):
                # start
                s_sum += stats[start[i]][start[j]] + stats[start[j]][start[i]]
                # link
                l_sum += stats[link[i]][link[j]] + stats[link[j]][link[i]]
        differ = min(differ, abs(s_sum-l_sum))
        return     
    
    for i in range(N):
        # i가 이미 start에 있거나, start에 i보다 큰 숫자가 들어가 있다면 생략
        if i in set(start): continue
        if start and start[-1] > i: continue
        cal_combi(idx+1, start + [i])
        
cal_combi(0)
print(differ)