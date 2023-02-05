import sys
input = sys.stdin.readline

word = input().rstrip()
words_list = []

for i in range(len(word)):
    words_list.append(word[i:])
    
words_list.sort()

print('\n'.join(words_list))