word = input()

count = 0
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


i = 0
while i < len(word):
    try:
        if word[i:i+2] == 'dz':
            if word[i:i+2] == word[-2:] and i == len(word) - 2:
                count += 2
                i += 2
            elif word[i+2] == '=':
                count += 1
                i += 3
            else:
                count += 1
                i += 1


        else:
            if word[i:i+2] in cro:
                count += 1
                i += 2
            else:
                count += 1
                i += 1
    except:
        break

print(count)
