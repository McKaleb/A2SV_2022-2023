class Solution:
    def isPalindrome(self, x: int) -> bool:
        xList = [*str(x)] #list
        xList.reverse()
        y = "".join(xList)
        if str(x) == y:
            return 1
        else:
            return 0
