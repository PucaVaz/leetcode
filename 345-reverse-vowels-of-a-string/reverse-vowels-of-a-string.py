class Solution:
    def reverseVowels(self, s: str) -> str:
        new_string = ""
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        lenS = len(s)
        i = 0
        j = lenS - 1  

        while i < lenS:
            if s[i] not in vowels:
                new_string += s[i]
                i += 1
                continue
            while s[j] not in vowels:
                j -= 1 
            new_string += s[j]
            j -= 1
            i += 1 
        
        return new_string