# DP : 인덱스를 뒤에서부터 하나씩 밟아나가자
import sys
input = sys.stdin.readline

T = int(input())
    
def max_profit(N, num_list):
    profit = 0
    max_price = num_list[-1] # 맨 마지막 날 값을 최댓값으로 설정
    for i in range(N-2,-1,-1): # 거꾸로 내려가면서 
        if num_list[i] > max_price: # 더 큰 값이 나오면 갱신
            max_price = num_list[i]
        elif num_list[i] < max_price: # 더 작은 값이 나오면 이익 추가
            profit += max_price-num_list[i]
    print(profit)
        
    
    
for _ in range(T):
    N = int(input())
    stock_list = list(map(int, input().split()))
    max_profit(N, stock_list)