class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        l1 = len(word1)
        l2 = len(word2)
        for i in range(max(l1,l2)):
            if l1==i:
                return ans + word2[i:]
            
            if l2==i:
                return ans + word1[i:]
            
            ans += word1[i] + word2[i]
        return ans


print(Solution().mergeAlternately('abc','pqr'))