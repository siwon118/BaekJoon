n = int(input())

count = 1

start = 1
diff = 6

while True:
    end = start + diff
    if n == 1:
        print(1)
        break

    if start <= n < end + 1:

        count += 1
        print(count)
        break

    count += 1
    start = end
    diff += 6
