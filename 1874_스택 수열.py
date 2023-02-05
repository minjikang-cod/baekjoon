import sys
input = sys.stdin.readline

N = int(input())
stack = []
num_list = [N-i for i in range(N)]
result = []
want = []
can = True

for _ in range(N):
    want.append(int(input()))

for w in want:
    if len(stack)==0:   
        stack.append(num_list.pop())
        result.append('+')
    while num_list and stack[-1] != w:
        stack.append(num_list.pop())
        result.append('+')
    
    if not(num_list) and stack[-1] != w:
        can = False
        break
    else:
        stack.pop()
        result.append('-')

if can:
    for r in result:    print(r)
else:
    print('NO')