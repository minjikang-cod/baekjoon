value = input()
value_list = list(map(lambda x : int(x), value.split(' ')))
isPrime = [True for i in range(value_list[1]+1)]

for num in range(value_list[1]+1):
    if num == 0 or num == 1:
        isPrime[num] = False
        continue
    if isPrime[num] == True:
        mul = 2
        notPrime = num*mul 
        while notPrime < len(isPrime):
           isPrime[notPrime] = False
           mul += 1 
           notPrime = num*mul

for i in range(value_list[0],value_list[1]+1):
    if isPrime[i]==True:
        print(i)