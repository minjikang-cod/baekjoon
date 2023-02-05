import sys

n = int(sys.stdin.readline())
solution = 0

start = n-len(list(str(n)))*9
end = n-len(list(str(n)))

for i in range(start,end):
    num_list = list(map(int,list(str(i))))
    decom = i + sum(num_list)
    if decom == n:
        solution = i
        break

print(solution)