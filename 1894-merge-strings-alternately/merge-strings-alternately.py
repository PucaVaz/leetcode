class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output =""
        j = 0
        k = 0
        for _ in range(min(len(word1),len(word2))):
            output += word1[j]
            j += 1 
            output += word2[k]
            k += 1
        
        while j < len(word1):
            output += word1[j]
            j += 1
        
        while k < len(word2):
            output += word2[k]
            k += 1

        return output
