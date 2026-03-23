import sys

input = sys.stdin.readline

n = int(input())
stack = []
result = []

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if stack:
            result.append(str(stack.pop()))
        else:
            result.append("-1")
    elif cmd[0] == "size":
        result.append(str(len(stack)))
    elif cmd[0] == "empty":
        if stack:
            result.append("0")
        else:
            result.append("1")
    elif cmd[0] == "top":
        if stack:
            result.append(str(stack[-1]))
        else:
            result.append("-1")

print("\n".join(result))