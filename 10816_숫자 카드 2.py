import sys
# 중복허용된 원소들이 들어오면 각 원소마다 몇개인지 세주는 라이브러리 : Counter
from collections import defaultdict
input = sys.stdin.readlines

lines = input()
num_dict = defaultdict(int)
for n in list(map(int, lines[1].split())):
    num_dict[n] += 1

find_list = list(map(int, lines[3].split()))
for f in find_list:
    print(num_dict[f], end = ' ')