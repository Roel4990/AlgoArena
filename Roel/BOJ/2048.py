import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    l, r = map(int, input().split())

    if r >= 4:
        print(r)
    elif l == 0:
        if r == 0:
            print(0)
        elif r == 3:
            print(5)
        else:
            print(2)
    elif l == 1:
        if r == 1:
            print(1)
        else:
            print(3)
    elif l == 2:
        if r == 2:
            print(2)
        elif r == 3:
            print(4)
    elif l == 3:
        print(3)
