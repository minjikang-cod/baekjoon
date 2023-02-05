import sys
from bisect import bisect_left
input = sys.stdin.readlines


lines = input()
N, M = map(int, lines[0].split()) 
num_list = []
for l in lines[1:]:
    num_list.append(int(l))
num_list.sort()

def find_mdiffer(M):
    if M == 0: # 무조건 자기 수 두번 고르면 됨
        return 0
    min_differ = 2000000000+1
    start, end = 0, bisect_left(num_list, M+num_list[0])
    while start < N and end < N:
        differ = num_list[end]-num_list[start]
        if differ == M:
            return M
        if differ > M:
            min_differ = min(differ, min_differ)
            start += 1
        else:
            end += 1
    
    return min_differ    

print(find_mdiffer(M))