import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# k개의 로프 w인 물체를 들어올림 - 각 로프 w/k의 중량
# 들어올릴 수 있는 물체의 최대 중량

# number of rope 
N = int(input())

weight = []
for _ in range(N):
    w = int(input())
    weight.append(w)

weight.sort(reverse=True)
answer = 0

for i in range(N):
    w = (i+1) * weight[i]
    answer = max(answer, w)

print(answer)