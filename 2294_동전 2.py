import sys
input = sys.stdin.readlines

lines = input()
n, k = map(int, lines[0].split())

coins = []
cnt_list = [0]*(k+1)
for i in range(1, n+1):
    coins.append(int(lines[i]))

for i in range(1, k+1):
    temp = []
    for c in coins:
        if i >= c and cnt_list[i-c] != -1:
            temp.append(cnt_list[i-c]+1)
    if not temp:
        cnt_list[i] = -1
    else:
        cnt_list[i] = min(temp)

print(cnt_list[k])