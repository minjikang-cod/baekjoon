import sys 
input = sys.stdin.readlines

lines = input()
left_child = {}
right_child = {}

for line in lines[1:]:
    p, l, r = line.split()
    left_child[p] = l
    right_child[p] = r
    
def preorder(root, sentence = ""):
    if root != '.':
        left = preorder(left_child[root],sentence)
        right = preorder(right_child[root],sentence)
        sentence += root + left + right
    return sentence

def inorder(root, sentence = ""):
    if root != '.':
        left = inorder(left_child[root],sentence)
        right = inorder(right_child[root],sentence)
        sentence += left + root + right
    return sentence

def postorder(root, sentence = ""):
    if root != '.':
        left = postorder(left_child[root],sentence)
        right = postorder(right_child[root],sentence)
        sentence += left + right + root
    return sentence

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))