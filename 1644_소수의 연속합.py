import sys
import math
input = sys.stdin.readline

def find_primes(n):
    is_prime = [0, 0] + [1 for _ in range(2, n+1)]
    prime_list = [2]
    
    for i in range(3, n+1, 2):
        if is_prime[i]:
            prime_list.append(i)
            
            j = 2
            while j*i <= n:
                is_prime[i*j] = 0; j += 1
    
    return prime_list

N = int(input())
prime_list = find_primes(N)

def find_sum(n):
    answer = 0
    lp = len(prime_list)
    start, end = 0, 1
    
    while end <= lp:
        temp = sum(prime_list[start:end])
        if temp < n:
            end += 1
        elif temp > n:
            start += 1
        elif temp == n:
            answer += 1
            end +=1
            
    return answer

print(find_sum(N))
