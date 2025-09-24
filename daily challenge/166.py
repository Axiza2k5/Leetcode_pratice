class Solution:
    def __init__(self):
        self.memo = []
    
    def getDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return ""
        dec = self._getDecimal(numerator, denominator)
        if ')' in dec:
            dec = '(' + dec
        if dec != "":
            return "." + dec
        return dec
        
    def _getDecimal(self, numerator: int, denominator: int) -> str:
        self.memo.append(numerator)
        dec = str(numerator//denominator)
        numerator %= denominator
        numerator *= 10

        if numerator == 0:
            return dec
        if numerator in self.memo:
            return dec + ')'
        
        return dec + self._getDecimal(numerator, denominator)

        
    def getInteger(self, numerator: int, denominator: int) -> str:
        return str(numerator//denominator)
    
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        return self.getInteger(numerator, denominator) + self.getDecimal((numerator%denominator)*10, denominator)
    
print(Solution().fractionToDecimal(666, 333))