n, x = map(int, (input().split()))
user_input = input()

a = ([int(x) for x in user_input.split()])

for i in range(len(a)):
    if a[i] < x:
        print(a[i], end=' ')
