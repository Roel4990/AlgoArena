import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0

for candidate in a:
    if candidate <= b:
        cnt = 1
    elif (candidate - b) % c == 0:
        cnt = 1 + (candidate - b) // c
    else:
        cnt = 2 + (candidate - b) // c

    answer += cnt
print(answer)