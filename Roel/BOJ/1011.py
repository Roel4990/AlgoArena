import sys
from math import sqrt
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    dt = y - x
    value = int(sqrt(dt))
    if dt <= value**2:
        print(value*2-1)
    elif dt <= value**2 + value:
        print(value*2)
    else:
        print(value*2+1)
