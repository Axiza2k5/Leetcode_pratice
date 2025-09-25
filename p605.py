class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        i = 0
        count = 0
        ln = len(flowerbed)
        while i < ln:
            if flowerbed[i]:
                i += 2
                continue

            if i == ln-1 and flowerbed[i] == 0:
                count += 1 
                break

            if flowerbed[i] == 0 and flowerbed[i+1]:
                i += 3
                continue

            flowerbed[i] = 1
            count += 1
            i += 2

        return n <= count

