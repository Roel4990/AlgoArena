import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
S = input()

# 문자열에서 'O'와 'X'의 개수를 셈
counter = Counter(S)

# O의 개수가 X의 개수 이상이면 Yes
print("Yes" if counter['O'] >= counter['X'] else "No")
