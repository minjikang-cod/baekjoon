# 재귀 : 스택 오버플로우 발생
# 파스칼의 삼각형 DP : 시간 초과
# 모듈로 연산 : (A*B)%P = (A%P*B%P)%P
# nCk = n*(n-1)*(n-2)*...*(n-k+1)/k*(k-1)*(k-2)*...*1

# 페르마의 소정리
# : p가 소수, a가 정수일 때 a^p 는 a(mod p)과 합동이다. -> p로 나눈 나머지가 서로 같다
# : 위 식의 양변을 a^2로 나눠주면 a^(p-2)는 1/a(mod p)와 합동이다.
# nCk % p = n!/(n-k)!k! % p = n!((n-k)!k!)^(p-2) % p

import sys
input = sys.stdin.readline
P = 1000000007

N, K = map(int, input().split())

fact_list = [1, 1]

for i in range(2, N+1):
    fact_list.append((i * fact_list[-1])%P)
    
top = fact_list[N]
bot = (fact_list[N-K] * fact_list[K]) % P

def power_modulo (num, k):
    if k == 0:
        return 1
    
    tmp = power_modulo(num, k//2)
    if k%2:
        return tmp * tmp * num % P
    else:
        return tmp * tmp % P

print((top % P) * (power_modulo(bot, P-2) % P) % P)