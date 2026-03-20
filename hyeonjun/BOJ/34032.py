import sys
input = sys.stdin.readline

N = int(input())

vote = list(input())
count_O = vote.count("O")

if count_O >= (N - count_O):
    print("Yes")

else:
    print("No")