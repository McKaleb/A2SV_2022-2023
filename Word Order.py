from collections import Counter

n = int(input())
words_list = []

for i in range(n):
    words = input()
    words_list.append(words)

counter = Counter(words_list)
occurence = ""

for word in counter:
    occurence += str(counter[word]) + " "

print(len(counter))
print(occurence)
