import sys 
input = sys.stdin.readlines

num_list = list(map(int, input()[1].split()))
index_dict = {x:idx for idx, x in enumerate(sorted(set(num_list)))}

result = [index_dict[x] for x in num_list]

print(*result)