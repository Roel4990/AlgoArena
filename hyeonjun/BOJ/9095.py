import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    answer = [0, 1, 2, 4]
    n = int(input())
    for i in range(4, n+1):
        answer.append(answer[i-1] + answer[i-2] + answer[i-3])
        #print(answer)
        #print(f"{i}:{answer[-1]}")
    print(answer[n])
