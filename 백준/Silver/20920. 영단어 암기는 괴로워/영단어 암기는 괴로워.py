from collections import defaultdict

n, m = map(int, input().split())

words = []
for i in range(n):
    words.append(input())

counts = defaultdict(int)
for word in words:
    if len(word) >= m:
        counts[word] += 1

value_sorted_counts = dict(sorted(counts.items(), key=lambda item: (-item[1], -len(item[0]), item[0])))

for key in value_sorted_counts.keys():
    print(key)
