import sys
input = sys.stdin.readline

def solve(what):
    global stack
    if what[0] == "push":
        stack.append(what[1])
    elif what[0] == "pop":
        print(stack.pop() if stack else -1)
    elif what[0] == "size":
        print(len(stack))
    elif what[0] == "top":
        print(stack[-1] if stack else -1)
    elif what[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)

N = int(input())
stack = []
for i in range(N):
    what = input().split()
    solve(what)
