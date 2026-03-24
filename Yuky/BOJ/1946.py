import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    applicants = [tuple(map(int, input().split())) for _ in range(n)]

    applicants.sort()

    # 서류 1등
    count = 1
    best_interview = applicants[0][1]

    for i in range(1, n):
        if applicants[i][1] < best_interview:
            count += 1
            best_interview = applicants[i][1]

    print(count)