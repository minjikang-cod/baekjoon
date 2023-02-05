# 유클리드 호제법을 이용하여 최대공약수 구하기
# 최소공배수 = 두 수를 곱한 후 최대공약수로 나누기

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
lcm = a * b

while (b!=0):
    temp = a % b
    a = b
    b = temp

gcf = a
lcm /= gcf

print(gcf)
print(int(lcm))