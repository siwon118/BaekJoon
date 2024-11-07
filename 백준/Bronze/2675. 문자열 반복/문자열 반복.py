n = int(input())

for _ in range(n):
    r, s = input().split()
    for i in range(len(s)):
        for j in range(int(r)):
            print(s[i], end='')
    print()
