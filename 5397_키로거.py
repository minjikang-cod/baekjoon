import sys
input = sys.stdin.readlines

for s in input()[1:]:
    pointer = 0
    left, right = [], []
    keyboard = list(s.rstrip())
    
    for key in keyboard:
        if key == '<':
            if left:
                right.append(left.pop())
        elif key == '>':
            if right:
                left.append(right.pop())
        elif key == '-':
            if left:
                left.pop()     
        else:
            left.append(key)
    
    left.extend(reversed(right))
    print(''.join(left))            