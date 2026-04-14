import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

dequeList = []

for _ in range(N):
    words = deque(input().split())
    dequeList.append(words)

L = deque(input().split())
while L:
    for i in range(N):
        if len(dequeList[i]) > 0:
            if L[0] == dequeList[i][0]:
                L.popleft()
                dequeList[i].popleft()
                break
    else:
        print("Impossible")
        break
else:
    for i in range(N):
        if len(dequeList[i]) != 0:
            print("Impossible")
            break
    else:
        print("Possible")