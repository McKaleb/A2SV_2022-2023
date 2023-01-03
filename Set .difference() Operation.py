# Enter your code here. Read input from STDIN. Print output to STDOUT
lenOfItem1 = input() #takes length of item
subStud = set(map(int, input().split()))
lenOfItem2 = input()
subStud2 = set(map(int, input().split()))

x = subStud.difference(subStud2)
print(len(x)) 
