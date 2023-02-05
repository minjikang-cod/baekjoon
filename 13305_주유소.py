import sys
input = sys.stdin.readlines

lines = input()

street = list(map(int, lines[1].split()))
oil = list(map(int, lines[2].split()))

min_oil = oil[0]
fee = street[0] * min_oil

for i in range(1, len(street)):
    min_oil = min(min_oil, oil[i])
    fee += street[i] * min_oil
    
print(fee)