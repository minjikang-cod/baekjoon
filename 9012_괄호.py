import sys
input = sys.stdin.readline

def is_vps(sentence):
    stack = 0
    for s in sentence:
        if s == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                return 'NO'
    if stack != 0:
        return 'NO'
    return 'YES'

for _ in range(int(input())):
    ps = input().rstrip() 
    print(is_vps(ps))