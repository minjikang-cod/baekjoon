import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
increase, decrease = [1]*N, [1]*N

for i in range(1, N):
    for j in range(i):
        # 증가하는 부분 수열
        if num_list[i] > num_list[j]:
            increase[i] = max(increase[i], increase[j]+1)
        # 감소하는 부분 수열(역순 증가하는 부분 수열)
        if num_list[-i-1] > num_list[-j-1]:
            decrease[-i-1] = max(decrease[-i-1], decrease[-j-1]+1)
        
total = [increase[i]+decrease[i]-1 for i in range(N)]
print(max(total))
