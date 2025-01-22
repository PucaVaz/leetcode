class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurrence = {}

        for i , c in enumerate(s):
            if c not in occurrence:
                occurrence[c] = [i, True]
            else:
                occurrence[c] = [i, False]

        for c in occurrence:
            if occurrence[c][1]:
                return occurrence[c][0]

        return -1