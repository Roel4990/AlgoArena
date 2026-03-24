import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    m.sort(key=lambda x: x[0])
    
    cnt = 0
    v = m[0][1]

    for i in m:
        if i[1] <= v:
            cnt += 1
            v = i[1]

    print(cnt)