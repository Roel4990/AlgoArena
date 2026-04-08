import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]
stack = []
result = []
next_num = 1

for i in numbers:
    while next_num <= i:
        stack.append(next_num)
        result.append("+")
        next_num += 1
    if stack[-1] == i:
        stack.pop()
        result.append("-")
    else:
        result = []
        break

print("\n".join(result) if result else "NO")
