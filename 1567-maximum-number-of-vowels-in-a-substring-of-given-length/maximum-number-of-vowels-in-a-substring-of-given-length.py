from collections import deque

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        current_vowels = deque()
        current_sum = 0
        max_vowels = 0

        if k == 0 or not s:
            return 0
        
        for i in range(k):
            value = 1 if s[i] in vowels else 0 
            current_vowels.append(value)
            current_sum += value

        max_vowels = current_sum
        if k >= len(s):
            return max_vowels

        for i in range(k, len(s)):
            if current_vowels:
                left_value = current_vowels.popleft()
                current_sum -= left_value

            right_value = 1 if s[i] in vowels else 0 
            current_vowels.append(right_value)
            current_sum += right_value
            max_vowels = max(max_vowels, current_sum)

        return max_vowels