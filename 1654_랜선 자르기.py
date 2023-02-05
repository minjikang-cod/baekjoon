import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan_list = []
for _ in range(K):
    lan_list.append(int(input().rstrip()))
    
lo, hi = 1, max(lan_list)

while lo <= hi:
    mid = (lo+hi)//2
    cnt = 0
    for lan in lan_list:
        cnt += lan//mid
    
    if cnt >= N:
        lo = mid + 1
    else:
        hi = mid - 1

print(hi) #왜 hi를 결괏값으로 출력해야하는가???