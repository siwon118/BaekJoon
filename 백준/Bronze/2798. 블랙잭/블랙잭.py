from itertools import combinations

n, m = map(int, input().split())
a = list(map(int, input().split()))

sorted_a = sorted(a, reverse=True)
sum_a = []

for comb in combinations(sorted_a, 3):
    if sum(comb) <= m:
        sum_a.append(sum(comb))


result = []
for v in sum_a:
    result.append(m-v)

print(sum_a[result.index(min(result))])
