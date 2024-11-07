array = []

count = 0
mod = set()

for i in range(10):
    array.append(int(input()))

for i in range(len(array)):
    mod.add(array[i] % 42)

print(len(mod))