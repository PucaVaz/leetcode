class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0

        for word in words:
            if len(word) < len(pref):
                continue
            for i in range(len(pref)): 
                if pref[i] != word[i]:
                    break
            else:
                result += 1 

        return result 