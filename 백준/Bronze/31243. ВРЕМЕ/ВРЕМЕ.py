a = []
time = []
number = []
temp = []

for i in range(3):
    a.append(input().split())
    if len(a[i][1]) == 1:
        a[i][1] = '0' + a[i][1]
    if len(a[i][3]) == 1:
        a[i][3] = '0' + a[i][3]
    time.append(''.join(a[i][0] + a[i][1]))
    time.append(''.join(a[i][2] + a[i][3]))

for i in range(len(time)):
        number.append(int(time[i]))

for i in range(0, (len(number)), 2):
    if number[i] > number[i+1]:
        number[i+1] += 2400
for i in range(0, len(number), 2):
    a = ((number[i] // 100) * 60 + (number[i] % 100))
    b = ((number[i+1] // 100) * 60 + (number[i+1] % 100))
    temp.append(b - a)

num_min = min(temp)
num_max = max(temp)

print(str(num_min // 60) + ":" + f'{num_min % 60:02d}')
print(str(num_max // 60) + ":" + f'{num_max % 60:02d}')