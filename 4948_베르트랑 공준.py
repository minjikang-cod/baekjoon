num_list = []
prime_list = []

num = int(input())

while num !=0 :
    num_list.append(num)
    num = int(input())

max_num = 2 * max(num_list)
is_prime = [True for _ in range(max_num+1)]

for i in range(max_num+1):
    if i==0 or i==1:
        is_prime[i] = False
    else:
        if is_prime[i]== True:
            j=2
            while(i*j<=max_num):
                is_prime[i*j]=False
                j += 1

for n in num_list:
    prime_sum = 0
    for k in range(n+1,2*n+1):
        prime_sum += is_prime[k]
    prime_list.append(prime_sum)

for p in prime_list:
    print(p)