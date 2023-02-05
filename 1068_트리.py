import sys
input = sys.stdin.readlines

lines = input()
parents = list(map(int, lines[1].split()))
erase = int(lines[2])

def erase_node(node, array):
    array[node] = -2  # 지웠음을 -2로 표현
    for i in range(len(array)):
        if array[i] == node: # 지워진 노드를 부모로 가지는 노드가 있다면
            erase_node(i, array) # 해당 노드들에 대해서도 erase 작업 수행

erase_node(erase, parents)
count = 0
for r in range(len(parents)):
    if parents[r] != -2 and r not in parents:
        count += 1
print(count)


    
    

