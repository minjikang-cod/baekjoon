# 문자열로 다뤄서 re로 부분문자 찾고 계속해서 새로운 문자열 생성하게 하면 시간초과 납니다
import sys
import re 
input = sys.stdin.readline 

string = input().rstrip()
bomb = input().rstrip()
stack = []

for i in range(len(string)):
    stack.append(string[i])
    if stack[-1] == bomb[-1]: # 마지막 글자가 같으면
        if ''.join(stack[-len(bomb):]) == bomb: # 문자열로 만들어서 다시 비교
            for _ in range(len(bomb)): stack.pop() 

print(''.join(stack) if stack else 'FRULA')