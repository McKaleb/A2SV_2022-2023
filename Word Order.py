from collections import Counter

n = int(input())
words_list = []

for i in range(n):
    words = input()
    words_list.append(words)

counter = Counter(words_list)

occ_num = []
dist_words = 0
for word in counter:
    occ_num.append(str(counter[word]))
    if counter[word] == 1:
        dist_words += 1 
    
occurence = " ".join(occ_num)
print(len(counter))
print(occurence
