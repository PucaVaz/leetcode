class Solution:
    def longestPalindrome(self, s: str) -> int:
        occurrences  = {}
        odd = 0
        
        for char in s:
            if char in occurrences:
                occurrences[char] += 1
            else:
                occurrences[char] = 1
        for element in occurrences:
            if occurrences[element] % 2 != 0:
                odd += 1
        
        if odd > 1:
            return len(s) - odd + 1
        else:
            return len(s)