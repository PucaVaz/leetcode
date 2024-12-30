class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        def count_chars(word):
            count = {}
            for char in word:
                count[char] = count.get(char, 0) + 1
            return count
        
        count1 = count_chars(word1)
        count2 = count_chars(word2)
        
        if set(count1.keys()) != set(count2.keys()):
            return False
        
        def get_frequency_counts(count):
            freq = {}
            for v in count.values():
                freq[v] = freq.get(v, 0) + 1
            return freq
        
        return get_frequency_counts(count1) == get_frequency_counts(count2)