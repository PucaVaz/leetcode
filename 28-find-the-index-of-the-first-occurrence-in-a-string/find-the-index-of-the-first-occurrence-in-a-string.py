class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        if len(needle) > len(haystack):
            return -1
    
        for i, char in enumerate(haystack):
            if char == needle[0]:
                if haystack[i: i + len(needle)] == needle:
                    return i
            
        return -1