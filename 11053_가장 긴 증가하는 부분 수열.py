import sys
input = sys.stdin.readlines

num_list = list(map(int, input()[1].split()))
lis_list = [1]*len(num_list)

for i in range(1, len(num_list)):
    for j in range(i):
        if num_list[i] > num_list[j]:
            lis_list[i] = max(lis_list[j]+1, lis_list[i])

print(max(lis_list))