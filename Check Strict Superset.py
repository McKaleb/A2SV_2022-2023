setA = set(input().split())
setN = int(input())

lst = []
for i in range(setN):
    set1 = set(input().split())
    if set1.intersection(setA) != set1 or set1 == setA:
        print("False")
        break
    lst.append(1)
if len(lst)==setN:
    print("True")
