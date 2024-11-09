n = int(input())

j = n-1
for i in range(1, n*2):
    m = 0
    if i % 2 == 1:
        print(' '*j, end='')
        print('*'*(i+m))
        m += 2
        j -= 1

j = 1
for i in range(1, n*2):
    m = n*2-2
    if i % 2 == 1:
        print(' '*j, end='')
        print('*'*(m-i))
        m += 2
        j += 1
