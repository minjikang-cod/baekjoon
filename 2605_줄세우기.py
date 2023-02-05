student = int(input())
value = input()
forward_list = list(map(lambda x : int(x), value.split(' ')))
standing = []

for s in range(student):
    standing.insert(max(0,s-forward_list[s]),s+1)

print(' '.join(map(lambda x : str(x), standing)))