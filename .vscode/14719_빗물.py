import sys 
input = sys.stdin.readline


def sum_rainfall():
    total_sum = 0
    hi, hb = 0, 0 # 가장 높은 블럭의 인덱스와 높이
    for i, b in enumerate(block):
        if b > hb:
            hi, hb = i, b 
    if hb == 0: return total_sum # 가장 높은 블럭의 높이가 0 이면 그냥 끝내버려 

    # 좌측 
    if hi > 0:      total_sum += func(hi, True)
    # 우측
    if hi < W-1:    total_sum += func (hi, False)
    return total_sum
    
''''''

def func(hi, isleft):
    rain_sum = 0
    if isleft: # 왼쪽에 대해 정리 
        lhi, lhb = 0, 0 
        for i in range(hi): # 왼쪽에서 가장 높은 위치 선택
            if block[i] > lhb:
                lhi, lhb = i, block[i] 
        
        for i in range(lhi+1, hi): # 빗물 양 덧셈
            rain_sum += lhb-block[i]
        
        if lhi != 0: # 가장 끝 쪽이 아니라면
            rain_sum += func(lhi, isleft)
    else: # 오른쪽에 대해 정리
        rhi, rhb = W-1, 0 # 가장 우측부터 탐색 예정
        for i in range(W-1, hi, -1):
            if block[i] > rhb:
                rhi, rhb = i, block[i]
                
        for i in range(hi+1, rhi):
            rain_sum += rhb-block[i]
        
        if rhi != W-1:
            rain_sum += func(rhi, isleft)
    
    return rain_sum
''''''
   
def another():
    total_sum = 0
    for i in range(1, W-1):
        leftmax, rightmax = max(block[:i]), max(block[i+1:])
        rainh = min(leftmax, rightmax) # 빗물은 낮은 벽 높이로 채워지기 때문
        
        if rainh > block[i]: # 기준 벽보다 낮으면 물이 차
            total_sum += rainh-block[i]
    return total_sum

''''''
H, W = map(int, input().split())
block = list(map(int, input().split()))
print(sum_rainfall())
print(another())



'''
4 4
3 0 1 4

가장 큰 값 4(Index : 3)-> 좌우 살펴
좌측 가장큰 값 3 (Index : 0)
-> (3-0) + (3-1) = 5

4 8
3 1 2 3 4 1 1 2

가장 큰 값 4 (Index : 4) -> 좌우 살펴
좌측 가장 큰 값 : 3 (4와 가장 먼 index값 : 0)
-> (3-1)+(3-2) = 3
우측 가장 큰 값 : 2(Index : 7)
-> (2-1)+(2-1) = 2 -> 5

3 5 
0 0 0 2 0
가장 큰 값 2 (3)
좌측 가장 큰 값 : 0 -> 없어
우측 가장 큰 값 : 0 -> 없어 

'''

'''
4 4
3 0 1 4

lm, rm = 3, 4
fin = 3
0<3 : result = 3

lm, rm = 3, 4
fin = 3
1 < 3 ; result = 3 + 2


4 8
3 1 2 3 4 1 1 2

lm, rm = 3, 4
fin = 3
1 < 3 : result = 2

lm, rm = 3, 4
fin = 3
2 < 3 : result = 2 + 1

lm, rm = 3, 4
fin = 3
3 == 3: ...

lm, rm = 3, 2
fin = 2
4 > 2 : ...

lm, rm = 4, 2
fin = 2
1 < 2 : result = 3 + 1

lm, rm = 4, 2
fin = 2
1 < 2 : result = 4 + 1

'''