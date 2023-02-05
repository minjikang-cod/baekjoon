import sys
input = sys.stdin.readlines

lines = input()
N = int(lines[0])
grape = [0] + [int(lines[i]) for i in range(1, N+1)] + [0]
drink = [0]*(N+2)

drink[1], drink[2] = grape[1], grape[1]+grape[2]

for i in range(3,N+1):
    # 무조건 해당 순서에 마시는게 아닐 수도 있으니까 이전 잔까지의 최댓값하고도 비교해야해
    drink[i] =  max(drink[i-1], 
                    drink[i-2]+grape[i], 
                    drink[i-3]+grape[i-1]+grape[i])

print(drink[N])