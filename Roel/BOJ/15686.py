import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

chickenPoints = []
housePoints = []
for r in range(1, N+1):
    rcs = list(map(int, input().split()))
    for c in range(1, N + 1):
        if rcs[c-1] == 1:
            housePoints.append((r, c))
        elif rcs[c-1] == 2:
            chickenPoints.append((r, c))

chickenPointsPositions = list(combinations(chickenPoints, M))
minValueResult = sys.maxsize
for chickenPointsPosition in chickenPointsPositions:
    minList = []
    for housePoint in housePoints:
        minValue = sys.maxsize
        for chickenPoint in chickenPointsPosition:
            distance = abs(chickenPoint[0] - housePoint[0]) + abs(chickenPoint[1] - housePoint[1])
            if distance < minValue:
                minValue = distance
        minList.append(minValue)
    if sum(minList) < minValueResult:
        minValueResult = sum(minList)
print(minValueResult)