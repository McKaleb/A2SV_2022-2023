from collections import defaultdict

abSize = list(map(int, input().split()))
aWords = defaultdict(list)
bWords = defaultdict(list)
for i in range(abSize[0]):
    aWords["A"].append(input())
for j in range(abSize[1]):
    bWords["B"].append(input())

for j in range(len(bWords["B"])):
    lst = []
    for i in range(len(aWords["A"])):
        if bWords["B"][j] == aWords["A"][i]:
            lst.append(i+1)
    if len(lst) == 0:
        lst.append(-1)
    print(*lst, sep=" ")
