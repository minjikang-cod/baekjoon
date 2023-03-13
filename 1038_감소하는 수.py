# 감소하는 수는 유한하다!!! → 최댓값 : 9876543210
# 조합 안 이용하는 코드 생각해봐,,,
from itertools import combinations 

N = int(input())
answers = []

for i in range(1, 11): # 한 자리수부터 열 자리수까지
    for c in combinations(range(10),i):
        c = list(c)
        c.sort(reverse = True)
        answers.append(int("".join(map(str, c))))

answers.sort()

try:
    print(answers[N])
except:
    print(-1)