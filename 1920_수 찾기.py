import sys
input = sys.stdin.readlines

lines = input()
num_list = list(map(int, lines[1].split()))
num_list.sort()
find_list = list(map(int, lines[3].split()))

def binary_search(goal, numbers):
    lo = 0; hi = len(numbers)-1
    answer = 0
    while lo <= hi:
        mid = (lo+hi)//2
        if numbers[mid] == goal:
            answer = 1; break
        elif numbers[mid] > goal:
            hi = mid-1
        else:
            lo = mid+1
    return answer

for f in find_list:
    print(binary_search(f, num_list))