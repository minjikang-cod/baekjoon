break_even_point = 0
value = input()
num = list(map(lambda x : int(x),value.split(' ')))

if num[2]-num[1]<=0:
    break_even_point = -1
else:
    break_even_point = num[0]/(num[2]-num[1]) + 1

print(int(break_even_point))