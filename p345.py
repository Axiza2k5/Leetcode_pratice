class Solution:
    def mergeAlternately(self, word1, word2) -> str:
        ans = ''
        l1 = len(word1)
        l2 = len(word2)
        i = 0
        j = 0
        while i < l1 or j < l2:
            if i<l1:
                ans += word1[i]
                i += 1
            if j<l2:
                ans += word2[j]
                j += 1

        return ans

    def reverseVowels(self, s: str) -> str:
        vowelsList = ['a','i','u','e','o','A','I','U','E','O']
        vowels = []
        strings = []
        last = 0
        ln = len(s)
        for i in range(ln):
            if s[i] in vowelsList:
                vowels.append(s[i])
                strings.append(s[last:i])
                last = i+1
        strings.append(s[last:])
        print(vowels)
        print(strings)
        print(self.mergeAlternately(strings, vowels[::-1]))
