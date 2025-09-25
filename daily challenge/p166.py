class Solution:
    def __init__(self):
        self.memo = []
        self.memo_index = {}
        self.numer = 0

    def getDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return ""
        dec = self._getDecimal(numerator, denominator, 1)
        if ')' in dec:
            dec = dec[:self.memo_index[self.numer]] + '(' + dec[self.memo_index[self.numer]:]
        if dec != "":
            return "." + dec
        return dec
        
    def _getDecimal(self, numerator: int, denominator: int, i: int) -> str:

        dec = str(numerator//denominator)
        numerator %= denominator

        if numerator == 0:
            return dec
        if numerator in self.memo:
            self.numer = numerator
            return dec + ')'
        
        self.memo.append(numerator)
        self.memo_index[numerator] = i
        numerator *= 10
        
        return dec + self._getDecimal(numerator, denominator, i+1)

        
    def getInteger(self, numerator: int, denominator: int) -> str:
        return str(numerator//denominator)
    
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        nev = ''
        if numerator < 0 and denominator < 0:
            numerator *= -1
            denominator *= -1
        elif numerator < 0:
            numerator *= -1
            nev = '-'
        elif denominator < 0 and numerator != 0:
            denominator *= -1
            nev = '-'

        return nev + self.getInteger(numerator, denominator) + self.getDecimal((numerator%denominator)*10, denominator)
