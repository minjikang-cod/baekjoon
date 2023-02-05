import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    nums = deque(list(map(int, input().split())))
    cnt = 0
    pmax = max(nums)
    while nums:
        p = nums.popleft()
        if p == pmax: # 가장 큰 문서중요도를 지녔을 경우
            cnt += 1
            N = N-1
            # 큐에 더이상 문서가 없거나 목표 문서를 출력했을 경우
            if N == 0 or M == 0: 
                break
            pmax = max(nums) # 문서 중요도 최댓값 업데이트
            M = M + len(nums) if M<0 else M - 1
        else:
            nums.append(p) # 다시 뒤에 붙이고 M 뒤로 넘기기
            M -= 1 
    print(cnt)