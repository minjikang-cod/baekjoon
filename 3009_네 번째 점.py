x_list = []
y_list = []
x = 0
y = 0

for _ in range(3):
    value = input()
    value_list = list(map(lambda x : int(x),value.split(' ')))
    x_list.append(value_list[0])
    y_list.append(value_list[1])

x_set = set(x_list)
y_set = set(y_list)

for i in x_set:
    if x_list.count(i) ==1:
        x = i

for j in y_set:
    if y_list.count(j) == 1:
        y = j
        
print(x, y, sep=' ')