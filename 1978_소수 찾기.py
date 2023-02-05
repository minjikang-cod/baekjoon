num = int(input())
value = input()
value_list = list(map(lambda x : int(x),value.split(' ')))
count = 0

for v in value_list:
    isPrime = True
    if v == 1:
        continue
    for i in range(2,v):
        if v%i == 0:
            isPrime = False
            break
    if isPrime:
        count += 1
    
print(count)  
    