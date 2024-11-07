stack = []

n = int(input())

for i in range(n):
    line = input()
    tokens = line.split(' ')

    if tokens[0] == 'push':
        stack.append(tokens[1])
    elif tokens[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif tokens[0] == 'size':
        print(len(stack))
    elif tokens[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif tokens[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
