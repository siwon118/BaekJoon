chess = [1, 1, 2, 2, 2, 8]
after = []

input_list = list(input().split())


for i in range(len(chess)):
    if chess[i] != input_list[i]:
        after.append(chess[i] - int(input_list[i]))
    else:
        after.append(0)

print(' '.join(str(s) for s in after))
