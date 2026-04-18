import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
stack = []
answer = []
num = 1

for i in numbers:
    while not stack or stack[-1] != i:
        if num > i:    
            print("NO")
            exit()
        else:
            stack.append(num)
            num += 1
            answer.append("+")

    stack.pop()
    answer.append("-")

for i in answer:
    print(i)    