import sys
input = sys.stdin.readlines

numbers = list(map(int, input()[1].split()))
numbers.sort()
for i in range(len(numbers)):
    numbers[i] *= (len(numbers)-i)
    
print(sum(numbers))