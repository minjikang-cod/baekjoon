import sys
input = sys.stdin.readline

minus_list = input().rstrip().split('-')

for m in range(len(minus_list)):
    mid = minus_list[m].split('+')
    cnt = 0
    for mm in mid:
        cnt += int(mm)
    minus_list[m] = cnt
    
if len(minus_list) != 1:
    for i in range(1, len(minus_list)):
        minus_list[0] -= minus_list[i]
        
print(minus_list[0])