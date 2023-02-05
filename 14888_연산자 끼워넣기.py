import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
# +, -, x, //
plus, minus, mul, div = map(int, input().split())
total_result = []

def operation(idx, result, plus, minus, mul, div):
    # 연산을 다 했다면 결과값 update
    if idx == N:
        total_result.append(result)
        return
    
    # addition
    if plus:
        operation(idx+1, result + num_list[idx], plus-1, minus, mul, div)
    # subtraction
    if minus:
        operation(idx+1, result - num_list[idx], plus, minus-1, mul, div)
    # multiplication
    if mul:
        operation(idx+1, result * num_list[idx], plus, minus, mul-1, div)
    # division
    if div:
        if result >= 0: tmp = result // num_list[idx]
        else:   tmp = -(-(result)//num_list[idx])
        operation(idx+1, tmp, plus, minus, mul, div-1)


operation(1, num_list[0], plus, minus, mul, div)
print(max(total_result))
print(min(total_result))