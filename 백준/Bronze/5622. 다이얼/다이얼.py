s = input()

count = 0

for i in s:
    if 65 <= ord(i) <= 67:
        count += 3
    elif 68 <= ord(i) <= 70:
        count += 4
    elif 71 <= ord(i) <= 73:
        count += 5
    elif 74 <= ord(i) <= 76:
        count += 6
    elif 77 <= ord(i) <= 79:
        count += 7
    elif 80 <= ord(i) <= 83:
        count += 8
    elif 84 <= ord(i) <= 86:
        count += 9
    elif 87 <= ord(i) <= 90:
        count += 10

print(count)
