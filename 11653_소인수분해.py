number = int(input())
factorization = []

while number != 1:
    for i in range(2,number+1):
        if number%i == 0:
            factorization.append(i)
            number = number//i
            break

for f in factorization:
    print(f)