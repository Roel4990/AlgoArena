import sys
input = sys.stdin.readline
def f(li):
    n = len(li)
    d = [1] * n
    for i in range(1, n):
        for j in range(i):
            if li[j] < li[i]:
                d[i] = max(d[i], d[j] + 1)
    return n - max(d)

n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
print(f(li))