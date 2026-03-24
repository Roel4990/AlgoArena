import sys

# 예제.txt
# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
stack = []

for input in sys.stdin:
		# .split() 문자열 나누기
    sp = input.split()

    if sp[0] == 'push':
		# .append() 리스트 맨 뒤에 값 추가
        stack.append(sp[1])
    elif sp[0] == 'pop':
        # .pop() 맨 뒤 값을 꺼내면서 삭제
        print(stack.pop() if stack else -1)
    elif sp[0] == 'size':
        print(len(stack))
    elif sp[0] == 'empty':
        print(0 if len(stack) else 1 )
    elif sp[0] == 'top':
		# stack[-1] 맨 뒤 값 확인
        print(stack[-1] if len(stack) else -1)