result = []

while True:

    count = 0

    stack = []

    s = input()

    if '-' in s:

        break

    for i in range(len(s)):

        if not stack and s[i] == '}':

            count += 1

            stack.append('{')

        elif stack and s[i] == '}':

            stack.pop()

        else:

            stack.append(s[i])

    count += len(stack)//2

    result.append(count)

for i in range(len(result)):

    print(i+1, ". ", result[i], sep='')