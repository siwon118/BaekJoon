n = int(input())
count = 0

while n > 0:
    words = input()
    used_list = []
    for i in range(len(words)-1):
        if words[i] != words[i+1]:
            used_list.append(words[i])
    used_list.append(words[-1])
    if len(used_list) == len(set(used_list)):
        count += 1
    n -= 1

print(count)
