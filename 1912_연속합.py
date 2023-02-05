import sys
input = sys.stdin.readlines

num_list = list(map(int, input()[1].split()))
#num_max = [num_list[0]]

for i in range(1,len(num_list)):
    num_list[i] = max(num_list[i], num_list[i-1]+ num_list[i])
#    num_max.append(num_list[i]+max(0,num_max[i-1]))

#print(max(num_max))
print(max(num_list))