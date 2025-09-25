class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ''
        length = len(s)
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        for i in range(numRows):
            for j in range(i, length, numRows*2 - 2):
                ans += s[j]
                if(i == numRows-1 or i == 0):
                    continue
                index = numRows*2 - 2 - i*2
                if j + index >= length:
                    continue
                ans += s[j+index]
        return ans


print(Solution().convert("PAYPALISHIRING", 4))
print(Solution().convert("A", 1))