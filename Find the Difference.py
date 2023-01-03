class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_S = Counter(s)
        freq_T = Counter(t)

        for key in freq_T.keys():
            if key not in freq_S or freq_S[key] != freq_T[key]:
                return key
        

        
# Time complexity - O(n)
# Space complexity - O(n)