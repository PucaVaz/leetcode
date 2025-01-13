class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
            words = s.split()
            list_pattern = list(pattern)

            if len(words) != len(list_pattern):
                return False
            seen = {} # key at the word, value is the pattern
            
            for i, word in enumerate(words):
                if word in seen:
                    if seen[word] != list_pattern[i]:
                        return False
                else:
                    if list_pattern[i] not in seen.values():
                        seen[word] = list_pattern[i]
                    else:
                        return False
            return True