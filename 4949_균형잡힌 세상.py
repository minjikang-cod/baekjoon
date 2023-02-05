import sys
input = sys.stdin.readlines

def balanced(sentence):
    stack = []
    for s in sentence:
        if s in '([':
            stack.append(s)
        elif s == ']':
            if not stack or stack.pop() != '[':
                return 'no'
        elif s == ')':
            if not stack or stack.pop() != '(':
                return 'no'
    
    if stack: return 'no'
    return 'yes'
    
for l in input()[:-1]:
    print(balanced(l.rstrip()))
