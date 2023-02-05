import math

value = input()
num = list(map(lambda x : int(x),value.split(' ')))
day = 1
if num[0] != num[1]:
    day = math.ceil((num[2]-num[1])/(num[0]-num[1]))
    
print(day)