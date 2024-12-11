class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = self._filter_string(s)
        reversed_string = self._reverse_string(filtered_string)

        if filtered_string != reversed_string:
            return False
        
        return True
  
    @staticmethod
    def _filter_string(s: str) -> str:
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        return new_s
    
    @staticmethod
    def _reverse_string(s: str) -> str:
        new_s = ""
        for i in range(len(s) - 1, -1, -1):
            new_s += s[i]

        return new_s
