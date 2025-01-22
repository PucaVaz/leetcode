class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurrence = {}

        for c in s:
            occurrence[c] = occurrence.get(c, 0) + 1
        
        for i, c in  enumerate(s):
            if occurrence[c] == 1:
                return i

        return -1
    