from collections import defaultdict

s = input()

word = s.upper()

words_dict = defaultdict(int)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


for i in range(len(word)):
    words_dict[word[i]] += 1

result = []
for key, value in words_dict.items():
    if value == max(words_dict.values()):
        result.append(key)

if len(result) > 1:
    print('?')
elif len(result) == 1:
    print(result.pop())
