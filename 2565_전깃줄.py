import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    num_list.append(list(map(int, input().split())))
# num_list를 첫번째 전깃줄 기준으로 정렬
num_list.sort(key = lambda x : x[0])
lis = [1]*N

for i in range(1, N):
    for j in range(i):
        if num_list[i][1] > num_list[j][1]:
            lis[i] = max(lis[i], lis[j]+1)

print(N-max(lis))
