n, m = map(int,input().split(' '))
number = list(map(int, input().split(' ')))
max_sum = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            temp_sum = number[i]+number[j]+number[k]
            if max_sum < temp_sum <= m:
                max_sum = temp_sum

print(max_sum)            