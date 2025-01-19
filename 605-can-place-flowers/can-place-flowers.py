class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        len_f = len(flowerbed)
        spaces = 0

        while i < len_f:
            if flowerbed[i] == 0 and \
                (i == 0 or flowerbed[i  - 1] == 0) and \
                (i == len_f - 1  or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                spaces += 1
            i += 1

        return spaces >= n