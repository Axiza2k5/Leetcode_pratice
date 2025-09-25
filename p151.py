class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split(' ')
        ln = len(s)
        i = 0
        while i < ln:
            if s[i] == '':
                s.pop(i) 
                ln = len(s)
                continue
            i += 1
        return ' '.join(s[::-1])