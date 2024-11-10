n = int(input())

member = {}


for _ in range(n):
    age, name = input().split()
    age = int(age)

    if age in member:
        member[age].append(name)
    else:
        member[age] = [name]

key_array = sorted(member.keys())

for i in key_array:
    if len(member[i]) > 1:
        for j in range(len(member[i])):
            print(i, ''.join(member[i][j]))
    else:
        print(i, ''.join(member[i]))
