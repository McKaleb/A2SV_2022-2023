if __name__ == '__main__':
    N = int(input())
    finalList = []
    for i in range(N):
        ans = input().split()
        if ans[0] == "insert":
            finalList.insert(int(ans[1]), int(ans[2]))
        elif ans[0] == "remove":
            finalList.remove(int(ans[1]))
        elif ans[0] == "append":
            finalList.append(int(ans[1]))
        elif ans[0] == "sort":
            finalList.sort()
        elif ans[0] == "pop":
            finalList.pop()
        elif ans[0] == "reverse":
            finalList.reverse()
        else:
            print(finalList)
