class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        maxCounter = 0 
        counter = 0

        i = 0 
        while i < len(s):
            c = s[i]
            if c in hashMap:
                counter = 0
                i = hashMap[c] + 1
                hashMap = {}
            else:
                hashMap[c] = i
                counter += 1
                i += 1
            
            if maxCounter <= counter:
                    maxCounter = counter

        return maxCounter
