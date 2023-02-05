import sys
input = sys.stdin.readlines

lines = input()
digits = []

for line in lines:
    digits.extend(line.split())
digits = sorted(list(map(lambda x : int(x[::-1]), digits[1:])))

for d in digits:
    print(d)