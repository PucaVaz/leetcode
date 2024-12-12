class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s_lower = s.lower()
        while l < r:
            if not s_lower[l].isalnum():
                l += 1
            elif not s_lower[r].isalnum():
                r -= 1
            elif s_lower[l] != s_lower[r]:
                return False
            else:
                l += 1
                r -= 1
        return True