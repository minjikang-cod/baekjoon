value = input()
isright = []

while value != '0 0 0':
    value_list = list(map(lambda x: int(x),value.split(' ')))
    max_index = value_list.index(max(value_list))
    residual_index = [0,1,2]
    residual_index.remove(max_index)
    ab = pow(value_list[residual_index[0]],2)+pow(value_list[residual_index[1]],2)
    if ab == pow(value_list[max_index],2):
        isright.append('right')
    else:
        isright.append('wrong')
    
    value = input()
        
for i in isright:
    print(i)