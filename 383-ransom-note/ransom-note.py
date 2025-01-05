class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        magazine_map = {}

        for c in magazine:
            magazine_map[c] = magazine_map.get(c, 0) + 1

        for c in ransomNote:
            if c in magazine_map:
                if magazine_map[c] == 0:
                    return False
                else:
                    magazine_map[c] = magazine_map.get(c, 0) - 1
            else:
                return False
        return True 
