class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = len(strs[0])
        k = 0
        ans = []
        for i in range(len(strs)):
            if len(strs[i]) < minLen:
                minLen = len(strs[i])
                k = i
        word = strs[k]
        for i in range(minLen):
            temp = True
            for j in range(len(strs)):
                if strs[j][i] != word[i]:
                    temp = False
                    break
            if not temp:
                break
            ans.append(word[i])
        return "".join(ans)
                    
            

        

                

