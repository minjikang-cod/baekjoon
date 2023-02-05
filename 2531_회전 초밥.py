import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi_list = [int(input()) for _ in range(N)]
sushi_list.extend(sushi_list[:k-1])

def max_sushi():
    answer = 0
    for i in range(N):
        temp = len(set(sushi_list[i:i+k]+[c]))
        if temp > answer:
            answer = temp
    
    return answer

print(max_sushi())