n = int(input())

a = []
for _ in range(n):
    a.append(input())

count = 0
score = 0

for i in range(len(a)):
    score = 0
    count = 0
    for j in range(len(a[i])-1):
        if a[i][j] == 'O':
            if score == 0:
                score = 1
            count += score

            if a[i][j] == a[i][j+1]:
                score += 1
        else:
            score = 0

    if len(a[i]) == 1 and a[i][0] == 'O':
        count += 1
    elif len(a[i]) > 1 and a[i][-1] == a[i][-2] and a[i][-1] == 'O':
        count += score
    elif len(a[i]) > 1 and a[i][-1] != a[i][-2] and a[i][-1] == 'O':
        count += 1


    print(count)
