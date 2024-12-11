class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) >= 0 and len(s) <= 2:
            return True
        
        if self.isPalindrome(s):
            return True

        l, r = 0, len(s) - 1 

        while l < r:
            if s[l] != s[r]:  
                skipL, skipR = s[l + 1: r + 1], s[l:r]
                return (self.isPalindrome(skipL) or self.isPalindrome(skipR))
            l, r = l + 1, r - 1
        return True
        
    @staticmethod 
    def isPalindrome(s: str) -> bool:
        return s == s[::-1]
