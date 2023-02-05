goal = int(input())
layer = 1
layer_num = 1
count = 1

while (goal>count):
    layer_num = layer * 6
    layer = layer + 1
    count = count + layer_num
    
print(layer)