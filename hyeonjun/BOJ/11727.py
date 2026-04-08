import sys
input = sys.stdin.readline

n = int(input())

answer = [0, 1]

for i in range(2, n+1):
    if i%2 == 0:
        answer.append(answer[i-1]*2 + 1)

    else:
        answer.append(answer[i-1]*2 - 1)

print(answer[n]%10007)
