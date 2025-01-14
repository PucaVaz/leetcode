class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
            s = list(s)
            t = list(t)
            if len(s) != len(t):
                return False
            seen = {} 
            
            for i, word in enumerate(s):
                if word in seen:
                    if seen[word] != t[i]:
                        return False
                else:
                    if t[i] not in seen.values():
                        seen[word] = t[i]
                    else:
                        return False
            return True