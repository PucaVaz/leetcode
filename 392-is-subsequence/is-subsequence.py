class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        ls = len(s)
        lt = len(t)
        while i < ls and j < lt:
            if s[i] == t[j]:
                i += 1
                j += 1
                continue
            j += 1
            
        if i < ls:
            return False
        return True