import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

chickenPoints = []
housePoints = []
for r in range(1, N + 1):
    for c, val in enumerate(map(int, input().split()), 1):
        if val == 1:
            housePoints.append((r, c))
        elif val == 2:
            chickenPoints.append((r, c))

minValueResult = sys.maxsize
for selectedChickens in combinations(chickenPoints, M):
    totalDistance = 0
    for hr, hc in housePoints:
        totalDistance += min(
            abs(cr - hr) + abs(cc - hc)
            for cr, cc in selectedChickens
        )
    if totalDistance < minValueResult:
        minValueResult = totalDistance

print(minValueResult)
