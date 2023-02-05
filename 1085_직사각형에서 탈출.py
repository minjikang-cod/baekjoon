value = input()
value_list = list(map(lambda x : int(x),value.split(' ')))
differ = [value_list[0],value_list[1],abs(value_list[0]-value_list[2]),abs(value_list[1]-value_list[3])]

print(min(differ))