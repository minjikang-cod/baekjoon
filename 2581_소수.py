M = int(input())
N = int(input())
prime_list = []

for num in range(M,N+1):
    isPrime = True
    if num == 1:
        continue
    for i in range(2,num):
        if num%i == 0:
            isPrime = False
            break
    if isPrime:
        prime_list.append(num)

if not prime_list:
    print(-1)
else:
    print(sum(prime_list))
    print(prime_list[0])