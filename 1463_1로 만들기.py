import sys
input = sys.stdin.readline

N = int(input())

#def make1(N):
#    if N==1: return 0
#    if N==2: return 1
#    
#    num_list = [0, 0, 1]
#    for i in range(3, N+1):
#        # % 결과를 더하는 것 : 3번(1을 뺀다) 연산의 횟수
#        # 해당 숫자보다 작은 수 중 가장 가까운 2,3의 배수에서의 최소 연산 수를 이용
#        # 마지막 +1 : 3 또는 2로 나누는 연산에 대한 횟수 한번 더하기
#        num_list.append(min(num_list[i//3]+i%3, num_list[i//2]+i%2)+1)
#    return num_list[N]


num_list = [0]*(N+1)

def make1_2(N): # 시간 덜 걸려
    if N == 1: return 0
    if num_list[N]: return num_list[N]
    
    if not N%6:
        num_list[N] = min(make1_2(N//2), make1_2(N//3))+1
    elif not N%2:
        num_list[N] = min(make1_2(N//2), make1_2(N-1))+1
    elif not N%3:
        num_list[N] = min(make1_2(N//3), make1_2(N-1))+1
    else:
        num_list[N] = make1_2(N-1)
    return num_list[N]
    
print(make1_2(N))