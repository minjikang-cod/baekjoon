import sys 
input = sys.stdin.readlines

num_list = list(map(int, input()[1].split()))
num_dict = dict(zip(range(len(num_list)),num_list))
sort_dict = sorted(num_dict.items(), key = lambda item: item[1])
index = 0
num_dict[sort_dict[0][0]] = 0

for n in range(1, len(sort_dict)):
    if sort_dict[n][1] != sort_dict[n-1][1]:
        index += 1
    num_dict[sort_dict[n][0]] = index

for k,v in num_dict.items():
    print(v, end=' ')